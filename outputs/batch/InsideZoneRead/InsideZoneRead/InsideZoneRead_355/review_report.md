# Play-Annotation-Generator Annotation Review — InsideZoneRead_355

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_355`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB3 | defense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | TE | offense | `12` | `11` |
| ✅ EXACT | `Action_ReadDefender` | TE | offense | `12` | `11` |
| ✅ EXACT | `Action_Keep` | TE | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | TE | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 26 |
| ✅ EXACT | `Action_BallSnap` | CB3 | `9` | `8` | 24 | START | 24 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `17` | 27 | START | 27 | 100 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `19` | `18` | 27 | START | 27 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 27 | START | 27 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `22` | `21` | 27 | START | 27 | 28 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `6` | 27 | START | 27 | 100 |
| ✅ EXACT | `Action_SnapReceive` | TE | `12` | `11` | 39 | END | 24 | 39 |
| ✅ EXACT | `Action_ReadDefender` | TE | `12` | `11` | 43 | START | 43 | 48 |
| ✅ EXACT | `Action_Keep` | TE | `12` | `11` | 49 | START | 49 | 76 |
| ✅ EXACT | `Action_BallCarry` | TE | `12` | `11` | 77 | START | 77 | 169 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 100 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 153 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 39 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 180 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 180 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 180 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 39 | 16 | inferred_complete_timeline |
| `Action_None` | 40 | 42 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 43 | 48 | 6 | inferred_complete_timeline |
| `Action_Keep` | 49 | 76 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 77 | 169 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 100 | 74 | inferred_complete_timeline |
| `Action_None` | 101 | 112 | 12 | inferred_complete_timeline |
| `Action_None` | 114 | 117 | 4 | inferred_complete_timeline |
| `Action_None` | 119 | 179 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 100 | 74 | inferred_complete_timeline |
| `Action_None` | 101 | 158 | 58 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 26 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 28 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 32 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 42 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 97 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 100 | 1 | inferred_complete_timeline |
| `Action_None` | 101 | 180 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 100 | 74 | inferred_complete_timeline |
| `Action_None` | 101 | 106 | 6 | inferred_complete_timeline |
| `Action_None` | 108 | 180 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 100 | 74 | inferred_complete_timeline |
| `Action_None` | 101 | 180 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 24 | 1 | inferred_complete_timeline |
| `Action_None` | 39 | 61 | 23 | inferred_complete_timeline |
| `Action_None` | 71 | 118 | 48 | inferred_complete_timeline |
| `Action_None` | 120 | 180 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 101 | 78 | inferred_complete_timeline |
| `Action_None` | 105 | 139 | 35 | inferred_complete_timeline |
| `Action_None` | 141 | 180 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 180 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 43 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 32 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 84 | 61 | inferred_complete_timeline |
| `Action_None` | 86 | 104 | 19 | inferred_complete_timeline |
| `Action_None` | 170 | 180 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 120 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 90 | 67 | inferred_complete_timeline |
| `Action_None` | 97 | 180 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_BallSnap` | 24 | 39 | 16 | inferred_complete_timeline |
| `Action_None` | 40 | 168 | 129 | inferred_complete_timeline |
| `Action_None` | 170 | 180 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 99 | 76 | inferred_complete_timeline |
| `Action_None` | 105 | 180 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 109 | 86 | inferred_complete_timeline |
| `Action_None` | 111 | 180 | 70 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 4–49 | 44 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 4–14 | 11 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 44–180 | 134 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 47–169 | 117 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 67–163 | 97 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 103–180 | 78 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 125–128 | 4 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 129–155 | 23 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 159–160 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 170–180 | 11 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 175–180 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 63 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [24-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-39] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-84] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-104] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-153] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-112] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-179] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-180] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-168] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-101] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-139] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [77-169] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-120] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-32] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 24, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [24-24] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-61] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [27-100] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-158] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [27-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-109] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-180] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-106] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-180] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [27-28] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [30-32] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [37-42] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [44-97] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-17] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-46] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-14] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-124] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-180] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-71] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-112] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-169] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-163] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-128] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-149] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_355'; source metadata written as null.

</details>
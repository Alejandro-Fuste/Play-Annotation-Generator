# Play-Annotation-Generator Annotation Review — InsideZoneRead_285

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_285`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 73
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | WR2 | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | WR1 | offense | `13` | `12` |
| ✅ EXACT | `Action_ReadDefender` | WR1 | offense | `13` | `12` |
| ✅ EXACT | `Action_Keep` | WR1 | offense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_BallSnap` | WR2 | `3` | `2` | 29 | START | 29 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `11` | `10` | 32 | START | 32 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `17` | `16` | 32 | START | 32 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `17` | 32 | START | 32 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 32 | START | 32 | 48 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `4` | 32 | START | 32 | 108 |
| ✅ EXACT | `Action_SnapReceive` | WR1 | `13` | `12` | 43 | END | 29 | 43 |
| ✅ EXACT | `Action_ReadDefender` | WR1 | `13` | `12` | 48 | START | 48 | 55 |
| ✅ EXACT | `Action_Keep` | WR1 | `13` | `12` | 56 | START | 56 | 77 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `13` | `12` | 78 | START | 78 | 91 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 108 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 60 | 32 | inferred_complete_timeline |
| `Action_None` | 64 | 180 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_SnapReceive` | 29 | 43 | 15 | inferred_complete_timeline |
| `Action_None` | 44 | 47 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 48 | 55 | 8 | inferred_complete_timeline |
| `Action_Keep` | 56 | 77 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 78 | 91 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_BallSnap` | 29 | 43 | 15 | inferred_complete_timeline |
| `Action_None` | 44 | 173 | 130 | inferred_complete_timeline |
| `Action_None` | 175 | 180 | 6 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 70 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 108 | 30 | inferred_complete_timeline |
| `Action_None` | 109 | 180 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 108 | 77 | inferred_complete_timeline |
| `Action_None` | 109 | 114 | 6 | inferred_complete_timeline |
| `Action_None` | 116 | 161 | 46 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 177 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 48 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 83 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 108 | 19 | inferred_complete_timeline |
| `Action_None` | 109 | 180 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 64 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 108 | 36 | inferred_complete_timeline |
| `Action_None` | 109 | 170 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 108 | 77 | inferred_complete_timeline |
| `Action_None` | 109 | 159 | 51 | inferred_complete_timeline |
| `Action_None` | 161 | 180 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 116 | 88 | inferred_complete_timeline |
| `Action_None` | 120 | 129 | 10 | inferred_complete_timeline |
| `Action_None` | 136 | 180 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 28 | 4 | inferred_complete_timeline |
| `Action_None` | 29 | 30 | 2 | inferred_complete_timeline |
| `Action_None` | 35 | 82 | 48 | inferred_complete_timeline |
| `Action_None` | 92 | 180 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 41 | 13 | inferred_complete_timeline |
| `Action_None` | 47 | 49 | 3 | inferred_complete_timeline |
| `Action_None` | 52 | 180 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 48 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 28 | 20 | inferred_complete_timeline |
| `Action_None` | 29 | 147 | 119 | inferred_complete_timeline |
| `Action_None` | 152 | 180 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 74 | 46 | inferred_complete_timeline |
| `Action_None` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_None` | 81 | 180 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 64 | 36 | inferred_complete_timeline |
| `Action_None` | 70 | 128 | 59 | inferred_complete_timeline |
| `Action_None` | 131 | 157 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 76 | 48 | inferred_complete_timeline |
| `Action_None` | 79 | 180 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 89 | 61 | inferred_complete_timeline |
| `Action_None` | 92 | 180 | 89 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–26 | 27 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 53–67 | 10 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 76–180 | 104 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 100–180 | 81 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 122–136 | 14 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 123–124 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 59 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [29-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-41] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-49] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-173] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-114] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-48] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-76] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-180] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-74] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-108] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-64] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-128] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-157] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [78-91] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-180] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-116] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-64] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-170] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-89] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-30] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-147] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-57] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-64] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-124] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-127] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-136] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_285'; source metadata written as null.

</details>
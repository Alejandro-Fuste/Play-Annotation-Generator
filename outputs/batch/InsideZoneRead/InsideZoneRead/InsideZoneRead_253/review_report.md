# Play-Annotation-Generator Annotation Review — InsideZoneRead_253

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_253`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_ReadDefender` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_Keep` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `22` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `3` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_BallSnap` | LG | `15` | `14` | 10 | START | 10 | 12 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `13` | `12` | 13 | START | 13 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `14` | `13` | 13 | START | 13 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `14` | 13 | START | 13 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 13 | START | 13 | 59 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `5` | `4` | 13 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | RG | `5` | `4` | 23 | END | 10 | 23 |
| ✅ EXACT | `Action_ReadDefender` | RG | `5` | `4` | 27 | START | 27 | 31 |
| ✅ EXACT | `Action_Keep` | RG | `5` | `4` | 32 | START | 32 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | `5` | `4` | 53 | START | 72 | 73 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 74 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 124 | 115 | inferred_complete_timeline |
| `Action_None` | 126 | 150 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 47 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 126 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 90 | 81 | inferred_complete_timeline |
| `Action_None` | 93 | 157 | 65 | inferred_complete_timeline |
| `Action_None` | 160 | 180 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 52 | 43 | inferred_complete_timeline |
| `Action_None` | 58 | 81 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 74 | 62 | inferred_complete_timeline |
| `Action_None` | 75 | 180 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 12 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 39 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 72 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 59 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 74 | 8 | inferred_complete_timeline |
| `Action_None` | 75 | 180 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 23 | 14 | inferred_complete_timeline |
| `Action_None` | 24 | 26 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 27 | 31 | 5 | inferred_complete_timeline |
| `Action_Keep` | 32 | 48 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 81 | 82 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 72 | 6 | inferred_complete_timeline |
| `Action_None` | 75 | 180 | 106 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 110 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 57 | 48 | inferred_complete_timeline |
| `Action_None` | 59 | 80 | 22 | inferred_complete_timeline |
| `Action_None` | 82 | 119 | 38 | inferred_complete_timeline |
| `Action_None` | 121 | 125 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 37 | 28 | inferred_complete_timeline |
| `Action_None` | 80 | 120 | 41 | inferred_complete_timeline |
| `Action_None` | 123 | 142 | 20 | inferred_complete_timeline |
| `Action_None` | 144 | 177 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 67 | 58 | inferred_complete_timeline |
| `Action_None` | 75 | 89 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 64 | 55 | inferred_complete_timeline |
| `Action_None` | 78 | 85 | 8 | inferred_complete_timeline |
| `Action_None` | 87 | 177 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 40 | 31 | inferred_complete_timeline |
| `Action_None` | 52 | 58 | 7 | inferred_complete_timeline |
| `Action_None` | 60 | 75 | 16 | inferred_complete_timeline |
| `Action_None` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 123 | 43 | inferred_complete_timeline |
| `Action_None` | 125 | 154 | 30 | inferred_complete_timeline |
| `Action_None` | 158 | 180 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 97 | 88 | inferred_complete_timeline |
| `Action_None` | 107 | 113 | 7 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 135 | 126 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 180 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 48–180 | 122 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 53–180 | 128 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 84–174 | 91 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 88–180 | 93 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 92–150 | 59 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 114–115 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 135–144 | 10 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 146–147 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 153–156 | 4 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 169–180 | 12 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 173–174 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `5` (RG)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 506: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '4' has invalid range: start=13, end=9. Clamping end to start.
- ⚠️ Action 'Action_None' range [10-126] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-52] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-81] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-97] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-113] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [32-48] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [72-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [81-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-124] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-47] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-64] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-85] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-177] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [13-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-72] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [13-39] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-57] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-119] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-125] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-40] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-75] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-37] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-142] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-177] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [13-59] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-63] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-90] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-157] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-97] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-180] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-174] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-144] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '32' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_253'; source metadata written as null.

</details>
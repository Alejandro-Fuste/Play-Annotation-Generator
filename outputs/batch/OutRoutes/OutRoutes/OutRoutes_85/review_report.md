# Play-Annotation-Generator Annotation Review — OutRoutes_85

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_85`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 67
- **Validation Warnings:** 70
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | WR2 | offense | `0` | `0` |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `9` | `Group` | 0 | START | 0 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `16` | `16` | 16 | START | 16 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 16 | START | 16 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 16 | START | 28 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 16 | START | 16 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | WR2 | `0` | `0` | 21 | START | 21 | 56 |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | `1` | `1` | 21 | START | 21 | 93 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 21 | END | 21 | 21 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 55 | START | 55 | 64 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `1` | `1` | 94 | START | 94 | 100 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `1` | `1` | 101 | START | 101 | 134 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 21 | 1 | inferred_complete_timeline |
| `Action_None` | 22 | 32 | 11 | inferred_complete_timeline |
| `Action_None` | 37 | 54 | 18 | inferred_complete_timeline |
| `Action_ThrowPass` | 55 | 64 | 10 | inferred_complete_timeline |
| `Action_None` | 65 | 125 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 158 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_RunOutRoute` | 21 | 93 | 73 | inferred_complete_timeline |
| `Action_SecureCatch` | 94 | 100 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 134 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_RunOutRoute` | 21 | 56 | 36 | inferred_complete_timeline |
| `Action_RunOutRoute` | 59 | 180 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–20
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 25 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 51 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 56 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 60 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 30 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 50 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 58 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 80 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 86 | 120 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 60 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 69 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 84 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 135 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 71 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 99 | 127 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 69 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 127 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 145 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 165 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 25 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 58 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 129 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 100 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 135 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 81 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 121 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 139 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `23` | Position_Unknown | Team_Unknown | 68–132 | 65 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 68–69 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 91–140 | 50 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 100–118 | 19 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 113–127 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunOutRoute` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 58 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_RunOutRoute' range [21-56] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [59-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-134] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-145] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-165] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-139] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-69] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-47] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-81] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-158] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-114] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-127] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-32] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-100] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-127] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-135] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-25] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-51] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-60] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-69] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [80-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-30] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [48-50] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [86-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-71] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [99-127] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-25] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-58] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-140] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-118] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-127] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>
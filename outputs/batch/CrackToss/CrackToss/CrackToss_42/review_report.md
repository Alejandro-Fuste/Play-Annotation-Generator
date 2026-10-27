# Play-Annotation-Generator Annotation Review — CrackToss_42

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_42`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 1
- **Action Segments:** 69
- **Validation Warnings:** 79
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RB | offense | `13` | `12` |
| ✅ EXACT | `Action_CrackBlock` | TE2 | offense | `4` | `3` |
| ✅ EXACT | `Action_PullBlock` | TE1 | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DE2 | defense | `16` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Toss` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `10` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `1` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 87 |
| ✅ EXACT | `Action_BallSnap` | RB | `13` | `12` | 88 | START | 88 | 95 |
| ✅ EXACT | `Action_CrackBlock` | TE2 | `4` | `3` | 91 | START | 91 | 101 |
| ✅ EXACT | `Action_PullBlock` | TE1 | `1` | `0` | 91 | START | 91 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DE2 | `16` | `15` | 91 | START | 91 | 110 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 95 | END | 88 | 95 |
| ✅ EXACT | `Action_Toss` | QB | `15` | `14` | 97 | START | 97 | 109 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `10` | `9` | 111 | START | 111 | 149 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_SnapReceive` | 88 | 95 | 8 | inferred_complete_timeline |
| `Action_None` | 96 | 96 | 1 | inferred_complete_timeline |
| `Action_Toss` | 97 | 109 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_BallSnap` | 88 | 95 | 8 | inferred_complete_timeline |
| `Action_None` | 96 | 179 | 84 | inferred_complete_timeline |
| `Action_None` | 181 | 200 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 122 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_BallCarry` | 111 | 149 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PullBlock` | 91 | 200 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_CrackBlock` | 91 | 101 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 200 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 200 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 87 | 41 | inferred_complete_timeline |
| `Action_None` | 88 | 110 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 194 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 178 | 91 | inferred_complete_timeline |
| `Action_None` | 183 | 187 | 5 | inferred_complete_timeline |
| `Action_None` | 189 | 200 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 157 | 70 | inferred_complete_timeline |
| `Action_None` | 159 | 200 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PullBlock` | 91 | 110 | 20 | inferred_complete_timeline |
| `Action_PullBlock` | 112 | 200 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 97 | 10 | inferred_complete_timeline |
| `Action_None` | 109 | 200 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 200 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 152 | 65 | inferred_complete_timeline |
| `Action_None` | 155 | 164 | 10 | inferred_complete_timeline |
| `Action_None` | 175 | 179 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 149 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 99 | 12 | inferred_complete_timeline |
| `Action_None` | 101 | 182 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–200 | 201 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 3–159 | 101 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 101–139 | 35 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 107–200 | 94 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 111–200 | 90 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 118–188 | 71 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 127–155 | 29 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 127–128 | 2 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 147–200 | 54 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 155–196 | 32 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 159–188 | 25 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 177–181 | 5 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 181–200 | 20 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 197–200 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `23` | `28` | 113 | 113 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 159 targets track ID '167', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 86: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '0' (TE1) duration 110 frames exceeds threshold 90 frames [start=91, end=200].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '15' (DE2) duration 110 frames exceeds threshold 90 frames [start=91, end=200].
- ⚠️ Action 'Action_PullBlock' range [91-200] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-194] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [91-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-200] for track '4' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-152] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-164] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-178] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-200] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [111-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-200] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-179] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-200] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-157] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-200] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [97-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [91-110] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [112-200] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-87] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-200] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-101] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-200] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-200] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-188] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-155] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-168] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-196] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-181] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-181] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-200] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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

</details>
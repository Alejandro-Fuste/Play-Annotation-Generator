# Play-Annotation-Generator Annotation Review — Counter_208

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_208`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | Team_Unknown | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_BallCarry` | QB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 25 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 26 | START | 26 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `11` | 28 | START | 38 | 52 |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | `15` | `14` | 28 | START | 34 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `7` | `6` | 28 | START | 28 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `20` | `19` | 28 | START | 71 | 77 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `3` | `2` | 28 | START | 28 | 53 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 37 | END | 26 | 37 |
| ⚠️ START CHANGED | `Action_BallCarry` | QB | `13` | `12` | 64 | START | 119 | 180 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 116 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 26 | 37 | 12 | inferred_complete_timeline |
| `Action_None` | 38 | 55 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 119 | 180 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 52 | 27 | inferred_complete_timeline |
| `Action_None` | 66 | 70 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 180 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 28 | 53 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_BallSnap` | 26 | 37 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 38 | 52 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 59 | 66 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_DownBlock` | 28 | 100 | 73 | inferred_complete_timeline |
| `Action_DownBlock` | 103 | 116 | 14 | inferred_complete_timeline |
| `Action_None` | 117 | 165 | 49 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 37 | 12 | inferred_complete_timeline |
| `Action_None` | 42 | 65 | 24 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 76 | 85 | 10 | inferred_complete_timeline |
| `Action_None` | 119 | 121 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 48 | 23 | inferred_complete_timeline |
| `Action_None` | 51 | 138 | 88 | inferred_complete_timeline |
| `Action_None` | 142 | 180 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 74 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 122 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 111 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 111 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 180 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 175 | 150 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 34–180 | 117 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 37–180 | 124 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 40–93 | 38 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 67–112 | 44 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 69–180 | 85 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 71–141 | 60 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 71–180 | 60 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 106–180 | 75 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 107–176 | 64 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 120–128 | 9 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 124–149 | 26 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 127–180 | 54 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 131–180 | 50 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 142–180 | 39 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 150–180 | 31 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 159–161 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `15` (Position_Unknown): Annotated start 28 != Inferred start 34
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `13` (QB): Annotated start 64 != Inferred start 119

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [26–37], lower_priority='Action_DownBlock' annotated_start=28, effective_Action_DownBlock_start=38.
- ⚠️ Action 'Action_None' range [26-111] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [28-53] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-48] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [28-100] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-74] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-52] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-70] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-111] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [38-52] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [59-66] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [119-180] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-37] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-65] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [34-89] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-109] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-42] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-51] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-93] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-126] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [71-77] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-167] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-128] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-149] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.

</details>
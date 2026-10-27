# Play-Annotation-Generator Annotation Review — Counter_200

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_200`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `15` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `12` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 31 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 32 | START | 32 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `12` | 36 | START | 57 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `14` | `13` | 36 | START | 36 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `5` | `4` | 36 | START | 36 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `15` | `14` | 36 | START | 36 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | `11` | `10` | 36 | START | 36 | 55 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 46 | END | 32 | 46 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `15` | 57 | START | 57 | 77 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `17` | `16` | 78 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 128 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_SnapReceive` | 32 | 46 | 15 | inferred_complete_timeline |
| `Action_None` | 47 | 56 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 57 | 77 | 21 | inferred_complete_timeline |
| `Action_None` | 78 | 120 | 43 | inferred_complete_timeline |
| `Action_None` | 122 | 173 | 52 | inferred_complete_timeline |
| `Action_None` | 175 | 225 | 51 | inferred_complete_timeline |
| `Action_None` | 228 | 235 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 74 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 36 | 55 | 20 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 58 | 68 | 11 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 70 | 128 | 59 | inferred_complete_timeline |
| `Action_None` | 129 | 175 | 47 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 213 | 9 | inferred_complete_timeline |
| `Action_None` | 222 | 227 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 74 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 59 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PullBlock` | 36 | 45 | 10 | inferred_complete_timeline |
| `Action_PullBlock` | 49 | 59 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 88 | 128 | 41 | inferred_complete_timeline |
| `Action_None` | 129 | 239 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 45 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 57 | 81 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 84 | 107 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 116 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_DownBlock` | 36 | 122 | 87 | inferred_complete_timeline |
| `Action_DownBlock` | 125 | 128 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_DownBlock` | 36 | 75 | 40 | inferred_complete_timeline |
| `Action_DownBlock` | 82 | 89 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 82 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 89 | 58 | inferred_complete_timeline |
| `Action_None` | 116 | 142 | 27 | inferred_complete_timeline |
| `Action_None` | 145 | 148 | 4 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 77 | 46 | inferred_complete_timeline |
| `Action_None` | 80 | 134 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 57 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 130 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 120 | 89 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 123 | 92 | inferred_complete_timeline |
| `Action_None` | 131 | 165 | 35 | inferred_complete_timeline |
| `Action_None` | 218 | 237 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 191 | 160 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 61–147 | 85 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 83–125 | 39 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 87–145 | 59 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 91–139 | 49 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 93–239 | 147 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 126–239 | 110 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 126–239 | 112 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 127–165 | 39 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 137–239 | 82 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 159–160 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 162–239 | 78 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 174–216 | 39 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 182–235 | 54 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 186–239 | 54 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 194–239 | 46 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 211–220 | 10 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 222–239 | 18 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 232–239 | 5 | 2 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `11` (3 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `17` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [32–46], lower_priority='Action_DownBlock' annotated_start=36, effective_Action_DownBlock_start=47.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (RG) duration 93 frames exceeds threshold 90 frames [start=36, end=128].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '14' (LG) duration 93 frames exceeds threshold 90 frames [start=36, end=128].
- ⚠️ Segment 'Action_BallCarry' for track '16' has invalid range: start=78, end=74. Clamping end to start.
- ⚠️ Action 'Action_None' range [32-123] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-165] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-237] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-191] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-130] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [36-75] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [82-89] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-57] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-82] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-77] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-134] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-59] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-89] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-142] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [36-55] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [58-68] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [70-128] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-213] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [32-45] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [57-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [84-107] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [110-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [36-122] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [125-128] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [36-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [49-59] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [57-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-225] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-235] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-103] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-104] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-194] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-213] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-218] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-165] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-205] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-235] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-220] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '34' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>
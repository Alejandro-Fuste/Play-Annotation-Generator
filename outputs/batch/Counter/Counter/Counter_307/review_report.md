# Play-Annotation-Generator Annotation Review — Counter_307

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_307`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `14` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 26 | START | 26 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `11` | 29 | START | 46 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `17` | `16` | 29 | START | 29 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `20` | `19` | 29 | START | 29 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `22` | `21` | 29 | START | 29 | 72 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `9` | `8` | 29 | START | 29 | 110 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 45 | END | 26 | 45 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `21` | `20` | 68 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 110 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 26 | 45 | 20 | inferred_complete_timeline |
| `Action_None` | 46 | 98 | 53 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 179 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 180 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 180 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 180 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 29 | 59 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 61 | 62 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 67 | 85 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 96 | 101 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 29 | 39 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 62 | 77 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 88 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 96 | 101 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 103 | 110 | 8 | inferred_complete_timeline |
| `Action_None` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_None` | 117 | 153 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_BallSnap` | 26 | 45 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 46 | 59 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 61 | 86 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 91 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PullBlock` | 29 | 72 | 44 | inferred_complete_timeline |
| `Action_PullBlock` | 76 | 80 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 96 | 110 | 15 | inferred_complete_timeline |
| `Action_None` | 111 | 131 | 21 | inferred_complete_timeline |
| `Action_None` | 150 | 180 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 29 | 110 | 82 | inferred_complete_timeline |
| `Action_None` | 111 | 180 | 70 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 112 | 87 | inferred_complete_timeline |
| `Action_None` | 114 | 116 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 180 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 61 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 169 | 144 | inferred_complete_timeline |
| `Action_None` | 171 | 180 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 180 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 180 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 179 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 165 | 140 | inferred_complete_timeline |
| `Action_None` | 168 | 180 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 180 | 155 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–61 | 62 | 2 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–180 | 181 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–46 | 47 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 55–180 | 116 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 67–180 | 114 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 71–179 | 106 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 87–180 | 66 | 7 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 111–180 | 70 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 116–180 | 65 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 127–133 | 5 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 131–180 | 50 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 162–167 | 6 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 162–180 | 19 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (3 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `21` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 616: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 616: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [26–45], lower_priority='Action_DownBlock' annotated_start=29, effective_Action_DownBlock_start=46.
- ⚠️ Segment 'Action_BallCarry' for track '20' has invalid range: start=68, end=46. Clamping end to start.
- ⚠️ Action 'Action_None' range [26-61] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-112] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-179] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-179] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-61] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [46-59] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [61-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [88-91] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-165] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-169] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [29-39] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [62-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [79-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [96-101] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-153] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-98] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [29-59] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [61-62] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [67-85] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [96-101] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [29-72] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [76-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [96-110] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-131] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-72] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-100] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-180] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-74] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-150] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-179] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-98] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-117] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-180] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-167] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>
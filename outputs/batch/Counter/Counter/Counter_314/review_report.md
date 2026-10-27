# Play-Annotation-Generator Annotation Review — Counter_314

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_314`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 125
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT2 | defense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 46 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 47 | START | 47 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `12` | 50 | START | 63 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `15` | `14` | 50 | START | 50 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `5` | `4` | 50 | START | 50 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `3` | `2` | 50 | START | 50 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `11` | `10` | 50 | START | 50 | 88 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 62 | END | 47 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `6` | `5` | 68 | START | 68 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT2 | `7` | `6` | 93 | START | 93 | 97 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 143 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–99
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 62 | 16 | inferred_complete_timeline |
| `Action_None` | 63 | 67 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 68 | 68 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 70 | 92 | 23 | inferred_complete_timeline |
| `Action_None` | 93 | 99 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 89 | 43 | inferred_complete_timeline |
| `Action_None` | 97 | 131 | 35 | inferred_complete_timeline |
| `Action_None` | 136 | 180 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_DownBlock` | 50 | 63 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 74 | 93 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 97 | 99 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_DownBlock` | 50 | 76 | 27 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 87 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 90 | 98 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 115 | 143 | 29 | inferred_complete_timeline |
| `Action_None` | 144 | 182 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_BallSnap` | 47 | 62 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 63 | 74 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 84 | 113 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 128 | 143 | 16 | inferred_complete_timeline |
| `Action_None` | 144 | 150 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PullBlock` | 50 | 77 | 28 | inferred_complete_timeline |
| `Action_PullBlock` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_PullBlock` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 102 | 143 | 42 | inferred_complete_timeline |
| `Action_None` | 144 | 191 | 48 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 200 | 5 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 50 | 88 | 39 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 93 | 102 | 10 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 106 | 112 | 7 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 143 | 143 | 1 | inferred_complete_timeline |
| `Action_None` | 144 | 144 | 1 | inferred_complete_timeline |
| `Action_None` | 147 | 172 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 54 | 8 | inferred_complete_timeline |
| `Action_None` | 58 | 76 | 19 | inferred_complete_timeline |
| `Action_None` | 79 | 128 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 94 | 48 | inferred_complete_timeline |
| `Action_None` | 110 | 122 | 13 | inferred_complete_timeline |
| `Action_None` | 201 | 210 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 104 | 58 | inferred_complete_timeline |
| `Action_None` | 106 | 119 | 14 | inferred_complete_timeline |
| `Action_None` | 122 | 132 | 11 | inferred_complete_timeline |
| `Action_None` | 134 | 210 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 93 | 97 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 118 | 210 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 131 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 66 | 20 | inferred_complete_timeline |
| `Action_None` | 68 | 139 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 61 | 15 | inferred_complete_timeline |
| `Action_None` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_None` | 77 | 80 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–186 | 185 | 3 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–137 | 126 | 4 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–202 | 162 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 70–164 | 95 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 95–200 | 106 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 104–132 | 29 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 106–116 | 11 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 127–209 | 73 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 129–210 | 69 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 131–210 | 79 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 140–159 | 9 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 141–210 | 69 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 146–209 | 62 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 149–204 | 51 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 179–183 | 5 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 184–204 | 20 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 191–209 | 19 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 198–199 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 82 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 630: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 630: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '2' (RG) duration 94 frames exceeds threshold 90 frames [start=50, end=143].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '4' (LG) duration 94 frames exceeds threshold 90 frames [start=50, end=143].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (C) duration 94 frames exceeds threshold 90 frames [start=50, end=143].
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [47–62], lower_priority='Action_DownBlock' annotated_start=50, effective_Action_DownBlock_start=63.
- ⚠️ Action 'Action_None' range [47-103] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-186] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-94] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-122] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [50-77] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [82-87] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [94-98] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-191] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [50-76] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [79-87] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [90-98] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-182] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' for track '5' starts at frame 68, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_Handoff' range [68-68] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-99] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [93-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [118-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-89] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-131] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-93] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-109] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-137] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-104] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-119] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [50-88] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [93-102] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [106-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '10' starts at frame 144, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [144-144] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-172] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-66] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [63-74] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [84-113] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-88] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-202] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [50-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [68-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [74-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [97-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-128] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-61] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-70] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-164] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-200] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-132] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-209] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-163] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-189] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-160] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-159] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-175] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-194] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-209] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-178] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-204] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-192] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-204] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-209] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>
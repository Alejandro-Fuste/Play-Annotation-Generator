# Play-Annotation-Generator Annotation Review — Counter_246

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_246`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DE2 | defense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE2 | defense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `3` | `2` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `10` | `9` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 19 |
| ✅ EXACT | `Action_BallSnap` | DE2 | `12` | `11` | 20 | START | 20 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE2 | `12` | `11` | 22 | START | 22 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `3` | `2` | 22 | START | 22 | 95 |
| ✅ EXACT | `Action_DownBlock` | RG | `4` | `3` | 22 | START | 22 | 95 |
| ✅ EXACT | `Action_PullBlock` | LG | `10` | `9` | 22 | START | 22 | 95 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `11` | `10` | 22 | START | 22 | 95 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 31 | END | 20 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `8` | `7` | 53 | START | 53 | 79 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 95 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 31 | 12 | inferred_complete_timeline |
| `Action_None` | 32 | 52 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 53 | 79 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 81 | 203 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 86 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 77 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 22 | 95 | 74 | inferred_complete_timeline |
| `Action_None` | 96 | 210 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PullBlock` | 22 | 95 | 74 | inferred_complete_timeline |
| `Action_None` | 96 | 180 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 22 | 95 | 74 | inferred_complete_timeline |
| `Action_None` | 96 | 129 | 34 | inferred_complete_timeline |
| `Action_None` | 131 | 133 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 22 | 95 | 74 | inferred_complete_timeline |
| `Action_None` | 96 | 154 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_BallSnap` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 22 | 34 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 37 | 41 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 44 | 47 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 49 | 81 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 83 | 95 | 13 | inferred_complete_timeline |
| `Action_None` | 96 | 139 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 139 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 27 | 8 | inferred_complete_timeline |
| `Action_None` | 30 | 36 | 7 | inferred_complete_timeline |
| `Action_None` | 41 | 43 | 3 | inferred_complete_timeline |
| `Action_None` | 56 | 57 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 115 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 55 | 36 | inferred_complete_timeline |
| `Action_None` | 57 | 60 | 4 | inferred_complete_timeline |
| `Action_None` | 67 | 86 | 20 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_None` | 94 | 131 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 103 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 64 | 45 | inferred_complete_timeline |
| `Action_None` | 66 | 131 | 66 | inferred_complete_timeline |
| `Action_None` | 143 | 210 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 75–173 | 91 | 2 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 102–210 | 89 | 4 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 105–210 | 106 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 125–163 | 28 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 126–127 | 2 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 127–163 | 24 | 6 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 132–151 | 19 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 133–147 | 15 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 138–150 | 6 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 170–171 | 2 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 173–175 | 3 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 177–178 | 2 | 1 | Undefined position; Undefined team |
| `28` | `45` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 194–197 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 494: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [20-55] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-60] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-86] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-131] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-77] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [22-95] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-129] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-103] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-64] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-131] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [53-79] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [81-203] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-86] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [22-34] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [37-41] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [44-47] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [49-81] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-27] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-173] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-141] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-159] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-144] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-163] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-137] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-163] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
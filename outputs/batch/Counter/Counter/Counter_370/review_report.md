# Play-Annotation-Generator Annotation Review — Counter_370

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_370`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 99
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `17` | `15` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `6` | `5` |
| ❌ MISSING SEGMENT | `Action_PullBlock` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 7 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 39 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `4` | 40 | START | 40 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `17` | `15` | 43 | START | 45 | 75 |
| ✅ EXACT | `Action_DownBlock` | RG | `6` | `5` | 43 | START | 43 | 57 |
| ❌ MISSING SEGMENT | `Action_PullBlock` | C | `5` | `4` | 43 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `14` | `13` | 43 | START | 43 | 69 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 52 | END | 40 | 52 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 63 | START | 63 | 74 |
| ✅ EXACT | `Action_BallCarry` | RB | `10` | `9` | 77 | START | 77 | 77 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 108 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 40 | 52 | 13 | inferred_complete_timeline |
| `Action_None` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_None` | 58 | 62 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 63 | 74 | 12 | inferred_complete_timeline |
| `Action_None` | 99 | 106 | 8 | inferred_complete_timeline |
| `Action_None` | 111 | 117 | 7 | inferred_complete_timeline |
| `Action_None` | 122 | 126 | 5 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 76 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 77 | 77 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 59 | 20 | inferred_complete_timeline |
| `Action_None` | 72 | 112 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 7–104
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 8 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 45 | 75 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 81 | 99 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 103 | 104 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_BallSnap` | 40 | 50 | 11 | inferred_complete_timeline |
| `Action_None` | 137 | 157 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_DownBlock` | 43 | 57 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 40 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 43 | 69 | 27 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 90 | 108 | 19 | inferred_complete_timeline |
| `Action_None` | 112 | 120 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 84 | 45 | inferred_complete_timeline |
| `Action_None` | 86 | 110 | 25 | inferred_complete_timeline |
| `Action_None` | 112 | 116 | 5 | inferred_complete_timeline |
| `Action_None` | 118 | 239 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 5–129
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 39 | 35 | inferred_complete_timeline |
| `Action_None` | 40 | 44 | 5 | inferred_complete_timeline |
| `Action_None` | 50 | 86 | 37 | inferred_complete_timeline |
| `Action_None` | 90 | 129 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 68 | 29 | inferred_complete_timeline |
| `Action_None` | 72 | 80 | 9 | inferred_complete_timeline |
| `Action_None` | 100 | 133 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 103 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 84 | 45 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_None` | 91 | 104 | 14 | inferred_complete_timeline |
| `Action_None` | 110 | 121 | 12 | inferred_complete_timeline |
| `Action_None` | 132 | 139 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 90 | 51 | inferred_complete_timeline |
| `Action_None` | 95 | 149 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 128 | 89 | inferred_complete_timeline |
| `Action_None` | 131 | 138 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 239 | 200 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–172 | 172 | 3 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 60–176 | 98 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 89–114 | 26 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 97–237 | 129 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 118–174 | 57 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 128–159 | 22 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 139–154 | 15 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 149–158 | 10 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 156–171 | 6 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 181–239 | 52 | 4 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 188–239 | 52 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 197–198 | 2 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 232–239 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (3 segments found)
- ❌ Missing segment for action `Action_PullBlock` on target `5` (C)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `14` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 742: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [40–52], lower_priority='Action_PullBlock' annotated_start=43, effective_Action_PullBlock_start=53.
- ⚠️ Action 'Action_None' range [40-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-138] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-84] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-110] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-172] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [40-50] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-157] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [43-57] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-103] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-104] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-139] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-59] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-112] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '9' starts at frame 77, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [77-77] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-90] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-149] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [40-52] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [63-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-106] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-80] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-40] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' for track '13' starts at frame 43, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PullLeadBlock' range [43-69] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [76-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [80-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [90-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-8] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [45-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [81-99] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [103-104] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-157] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-176] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-114] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-221] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-174] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-158] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-205] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-234] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>
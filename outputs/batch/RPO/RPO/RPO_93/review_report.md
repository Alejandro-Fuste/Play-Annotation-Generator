# Play-Annotation-Generator Annotation Review — RPO_93

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `RPO_93`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 167
- **Validation Errors:** 1
- **Overall Status:** FAILED
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `30` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `3` | `3` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `3` | `3` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 26 | START | 26 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 26 | START | 26 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 26 | START | 26 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 26 | START | 26 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 26 | START | 26 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 26 | START | 26 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 26 | START | 26 | 264 |
| ✅ EXACT | `Action_ReadDefender` | QB | `3` | `3` | 70 | START | 70 | 86 |
| ✅ EXACT | `Action_PullBall` | QB | `3` | `3` | 87 | START | 87 | 104 |
| ✅ EXACT | `Action_ThrowPass` | QB | `3` | `3` | 120 | START | 120 | 128 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 26–156
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 69 | 44 | inferred_complete_timeline |
| `Action_ReadDefender` | 70 | 86 | 17 | inferred_complete_timeline |
| `Action_PullBall` | 87 | 104 | 18 | inferred_complete_timeline |
| `Action_None` | 105 | 119 | 15 | inferred_complete_timeline |
| `Action_ThrowPass` | 120 | 128 | 9 | inferred_complete_timeline |
| `Action_None` | 129 | 144 | 16 | inferred_complete_timeline |
| `Action_None` | 146 | 156 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 26–177
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 93 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 110 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 126 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 177 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 26–78
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 57 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 78 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 26–182
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 64 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 73 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 87 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 113 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 182 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 26–146
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 71 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 84 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 111 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 116 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 146 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 26–108
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 88 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 99 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 108 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 26–264
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 264 | 239 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 26–360
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 360 | 335 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 26–74
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 74 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 44–67
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 44 | 67 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 26–104
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 79 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 104 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 26–389
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 68 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 128 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 360 | 231 | inferred_complete_timeline |
| `Action_PreSnap` | 362 | 389 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 26–133
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 69 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 121 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 133 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 26–98 | 70 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 26–182 | 95 | 5 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 70–168 | 95 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 75–136 | 57 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 87–114 | 27 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 90–217 | 125 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 90–188 | 67 | 6 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 112–367 | 199 | 7 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 114–159 | 46 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 117–122 | 6 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 129–154 | 20 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 131–266 | 131 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 137–138 | 2 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 139–158 | 8 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 141–382 | 223 | 5 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 141–177 | 37 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 157–177 | 21 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 163–267 | 100 | 3 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 174–178 | 5 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 209–368 | 146 | 4 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 225–348 | 96 | 4 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 237–389 | 149 | 3 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 252–292 | 41 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 261–287 | 25 | 3 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 285–389 | 96 | 4 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 306–389 | 84 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 365–389 | 25 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 381–389 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['C', 'LG', 'LT', 'RG'].

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 109 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 172: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [26-93] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-110] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-126] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-177] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-90] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-98] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-57] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-78] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-144] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-156] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-69] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-121] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-133] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-64] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-73] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-113] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-123] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-182] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-88] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-99] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-108] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-360] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-79] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-264] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-71] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-111] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-123] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-68] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-128] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-360] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-74] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-182] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-67] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-116] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-136] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-114] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-208] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-217] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-126] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-159] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-169] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-172] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-178] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-188] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-139] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-157] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-161] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-367] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-154] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-135] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-152] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-266] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-138] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-140] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-144] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-158] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-163] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-170] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-349] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-382] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-177] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-177] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-252] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-261] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-267] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-178] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-265] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-275] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-337] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-368] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-236] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-247] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-319] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-348] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-242] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-338] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-389] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-292] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-265] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-268] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-287] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-308] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-325] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-338] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>
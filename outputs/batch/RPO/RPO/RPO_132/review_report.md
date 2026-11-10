# Play-Annotation-Generator Annotation Review — RPO_132

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_132`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 63
- **Ball Tracks:** 0
- **Action Segments:** 153
- **Validation Warnings:** 211
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `28` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 137
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `11` | `11` | 81 | START | 81 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `16` | 81 | START | 81 | 87 |
| ✅ EXACT | `Action_ZoneBlock` | C | `4` | `4` | 81 | START | 81 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `7` | 81 | START | 81 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `8` | `8` | 81 | START | 81 | 104 |
| ✅ EXACT | `Action_ReadDefender` | QB | `6` | `6` | 89 | START | 89 | 98 |
| ✅ EXACT | `Action_PullBall` | QB | `6` | `6` | 99 | START | 99 | 110 |
| ✅ EXACT | `Action_ThrowPass` | QB | `6` | `6` | 133 | START | 133 | 140 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 88 | 9 | inferred_complete_timeline |
| `Action_ReadDefender` | 89 | 98 | 10 | inferred_complete_timeline |
| `Action_PullBall` | 99 | 110 | 12 | inferred_complete_timeline |
| `Action_None` | 111 | 132 | 22 | inferred_complete_timeline |
| `Action_ThrowPass` | 133 | 140 | 8 | inferred_complete_timeline |
| `Action_None` | 141 | 169 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 125 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 148 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 104 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 140 | 33 | inferred_complete_timeline |
| `Action_None` | 141 | 159 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 114 | 34 | inferred_complete_timeline |
| `Action_None` | 145 | 151 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 127 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 87 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_None` | 146 | 163 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 110 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 116 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 140 | 15 | inferred_complete_timeline |
| `Action_None` | 141 | 150 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 171 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 134 | 55 | inferred_complete_timeline |
| `Action_None` | 136 | 146 | 11 | inferred_complete_timeline |
| `Action_None` | 148 | 154 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 157 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 90 | 11 | inferred_complete_timeline |
| `Action_None` | 92 | 111 | 20 | inferred_complete_timeline |
| `Action_None` | 117 | 211 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 151 | 72 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 153 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 389 | 310 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 216 | 137 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–155 | 143 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 79–97 | 16 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 85–144 | 51 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 107–130 | 24 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 140–169 | 30 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 148–158 | 11 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 154–156 | 3 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 168–366 | 199 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 173–389 | 212 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 178–188 | 11 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 193–224 | 23 | 4 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 199–205 | 7 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 200–203 | 4 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 202–206 | 5 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 202–208 | 7 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 204–206 | 3 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 204–205 | 2 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 218–336 | 52 | 6 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 231–378 | 95 | 6 | Undefined position; Undefined team |
| `37` | `56` | Position_Unknown | Team_Unknown | 235–246 | 11 | 2 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 245–389 | 56 | 6 | Undefined position; Undefined team |
| `40` | `60` | Position_Unknown | Team_Unknown | 245–267 | 23 | 1 | Undefined position; Undefined team |
| `41` | `62` | Position_Unknown | Team_Unknown | 249–369 | 76 | 4 | Undefined position; Undefined team |
| `42` | `63` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `43` | `64` | Position_Unknown | Team_Unknown | 260–298 | 17 | 4 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 266–267 | 2 | 1 | Undefined position; Undefined team |
| `45` | `68` | Position_Unknown | Team_Unknown | 273–295 | 23 | 1 | Undefined position; Undefined team |
| `46` | `69` | Position_Unknown | Team_Unknown | 281–322 | 28 | 5 | Undefined position; Undefined team |
| `47` | `70` | Position_Unknown | Team_Unknown | 281–303 | 23 | 1 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 288–303 | 16 | 1 | Undefined position; Undefined team |
| `49` | `72` | Position_Unknown | Team_Unknown | 293–382 | 90 | 1 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 303–389 | 87 | 1 | Undefined position; Undefined team |
| `51` | `75` | Position_Unknown | Team_Unknown | 306–389 | 84 | 1 | Undefined position; Undefined team |
| `52` | `81` | Position_Unknown | Team_Unknown | 322–384 | 45 | 7 | Undefined position; Undefined team |
| `53` | `83` | Position_Unknown | Team_Unknown | 324–389 | 65 | 2 | Undefined position; Undefined team |
| `54` | `85` | Position_Unknown | Team_Unknown | 328–389 | 62 | 1 | Undefined position; Undefined team |
| `55` | `86` | Position_Unknown | Team_Unknown | 341–389 | 40 | 4 | Undefined position; Undefined team |
| `56` | `87` | Position_Unknown | Team_Unknown | 342–389 | 48 | 1 | Undefined position; Undefined team |
| `57` | `88` | Position_Unknown | Team_Unknown | 351–389 | 39 | 1 | Undefined position; Undefined team |
| `58` | `90` | Position_Unknown | Team_Unknown | 352–380 | 27 | 3 | Undefined position; Undefined team |
| `59` | `93` | Position_Unknown | Team_Unknown | 361–386 | 18 | 2 | Undefined position; Undefined team |
| `60` | `94` | Position_Unknown | Team_Unknown | 364–382 | 18 | 2 | Undefined position; Undefined team |
| `61` | `95` | Position_Unknown | Team_Unknown | 381–386 | 6 | 1 | Undefined position; Undefined team |
| `62` | `96` | Position_Unknown | Team_Unknown | 381–389 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 47 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 47 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 94 |
| Missing visible bounding boxes during action | 115 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 242: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_None' range [80-153] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-151] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-127] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-216] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [99-110] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-114] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-151] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-104] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-157] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-125] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-110] for track '11' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [113-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-134] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-146] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-154] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-140] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-111] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-211] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-163] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-86] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-97] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-130] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-158] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-366] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-308] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-376] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-384] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-188] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-209] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-205] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-208] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-255] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-274] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-378] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-242] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-257] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-271] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-307] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-369] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-389] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-267] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-314] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-355] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-369] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-289] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-298] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-295] for track '45' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-293] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-309] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-322] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-303] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-303] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-382] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-327] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-332] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-343] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-356] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-380] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-357] for track '55' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-375] for track '55' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-385] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-359] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-376] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-371] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-386] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-370] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-382] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-386] for track '61' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.

</details>
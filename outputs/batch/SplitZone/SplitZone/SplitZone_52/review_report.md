# Play-Annotation-Generator Annotation Review — SplitZone_52

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_52`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 129
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | offense | `24` | `24` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `14` | `14` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `0` | `Group` | 9 | START | 10 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 9 | START | 10 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 9 | START | 22 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 9 | START | 29 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `24` | `Group` | 9 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 9 | START | 10 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 9 | START | 10 | 97 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 93 | START | 93 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `0` | `0` | 96 | START | 96 | 157 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `1` | 96 | START | 96 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `15` | 96 | START | 108 | 121 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | `24` | `24` | 96 | START | 172 | 172 |
| ✅ EXACT | `Action_SplitBlock` | TE | `9` | `9` | 98 | START | 98 | 106 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `6` | 107 | END | 93 | 107 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `6` | 111 | START | 111 | 119 |
| ✅ EXACT | `Action_BallCarry` | RB | `14` | `14` | 120 | START | 120 | 122 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `4` | `4` | 135 | START | 135 | 170 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 170 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 10–137
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 92 | 83 | inferred_complete_timeline |
| `Action_SnapReceive` | 93 | 107 | 15 | inferred_complete_timeline |
| `Action_None` | 108 | 110 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 111 | 119 | 9 | inferred_complete_timeline |
| `Action_None` | 120 | 126 | 7 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 22–122
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 114 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 119 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 120 | 122 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 10–106
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 97 | 88 | inferred_complete_timeline |
| `Action_SplitBlock` | 98 | 106 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 10–195
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 95 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 170 | 75 | inferred_complete_timeline |
| `Action_None` | 171 | 184 | 14 | inferred_complete_timeline |
| `Action_None` | 186 | 195 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 10–193
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 39 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 95 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 157 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 170 | 4 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 175 | 193 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 29–172
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 31 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 92 | 59 | inferred_complete_timeline |
| `Action_BallSnap` | 93 | 107 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 121 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 170 | 41 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `24`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 172–173
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 172 | 172 | 1 | inferred_complete_timeline |
| `Action_None` | 173 | 173 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 10–144
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 12 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 78 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_None` | 93 | 135 | 43 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 10–312
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 92 | 83 | inferred_complete_timeline |
| `Action_None` | 93 | 227 | 135 | inferred_complete_timeline |
| `Action_None` | 236 | 312 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 10–324
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 92 | 83 | inferred_complete_timeline |
| `Action_None` | 93 | 141 | 49 | inferred_complete_timeline |
| `Action_None` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_None` | 155 | 160 | 6 | inferred_complete_timeline |
| `Action_None` | 184 | 293 | 110 | inferred_complete_timeline |
| `Action_None` | 295 | 300 | 6 | inferred_complete_timeline |
| `Action_None` | 303 | 324 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 10–171
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 81 | 72 | inferred_complete_timeline |
| `Action_None` | 93 | 171 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 13–204
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 92 | 80 | inferred_complete_timeline |
| `Action_None` | 93 | 204 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 10–359
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 45 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 92 | 46 | inferred_complete_timeline |
| `Action_None` | 93 | 101 | 9 | inferred_complete_timeline |
| `Action_None` | 114 | 136 | 23 | inferred_complete_timeline |
| `Action_None` | 186 | 359 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 10–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 92 | 83 | inferred_complete_timeline |
| `Action_None` | 93 | 193 | 101 | inferred_complete_timeline |
| `Action_None` | 198 | 359 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 14–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 92 | 79 | inferred_complete_timeline |
| `Action_None` | 93 | 359 | 267 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 10–151 | 135 | 4 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 10–195 | 186 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 111–116 | 6 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 124–162 | 29 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 144–220 | 70 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 150–359 | 190 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 150–183 | 34 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 151–179 | 29 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 156–202 | 47 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 166–351 | 186 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 178–359 | 160 | 4 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 184–353 | 111 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 188–210 | 22 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 226–359 | 131 | 4 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 232–359 | 126 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 267–359 | 93 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 278–359 | 82 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 281–292 | 12 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 285–359 | 68 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 289–321 | 26 | 2 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 294–359 | 66 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 332–355 | 24 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 333–359 | 25 | 3 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 340–359 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `0` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `24` (RG): Annotated start 96 != Inferred start 172

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [93–107], lower_priority='Action_ZoneBlock' annotated_start=96, effective_Action_ZoneBlock_start=108.
- ⚠️ Segment 'Action_ZoneBlock' for track '24' has invalid range: start=172, end=170. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [10-39] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-157] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-165] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-170] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-193] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-184] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-195] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-121] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-144] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-227] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-312] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-141] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-293] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-300] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-324] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-92] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-81] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [98-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-45] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-12] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-78] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-204] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-114] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-119] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [120-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-92] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-121] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-184] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-220] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-158] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-183] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-202] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-351] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '24' starts at frame 173, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [173-173] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-271] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-330] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-341] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-272] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-353] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-249] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-325] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-348] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-359] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-292] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-311] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-355] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-356] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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

</details>
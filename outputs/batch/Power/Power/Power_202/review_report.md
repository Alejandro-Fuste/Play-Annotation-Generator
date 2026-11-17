# Play-Annotation-Generator Annotation Review — Power_202

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_202`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 25
- **Ball Tracks:** 1
- **Action Segments:** 78
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 11 | START | 11 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 11 | START | 11 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 11 | START | 11 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 11 | START | 11 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 11 | START | 11 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 11 | START | 11 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 11 | START | 11 | 172 |
| ✅ EXACT | `Action_DownBlock` | RG | `11` | `11` | 116 | START | 116 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `4` | `4` | 116 | START | 116 | 148 |
| ✅ EXACT | `Action_DownBlock` | C | `8` | `8` | 116 | START | 116 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `3` | `3` | 116 | START | 116 | 129 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 11–299
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 46 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 151 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 167 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 240 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 264 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 299 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 11–299
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 172 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 183 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 210 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 299 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 11–190
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 155 | 145 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 190 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 11–299
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 115 | 105 | inferred_complete_timeline |
| `Action_PullBlock` | 116 | 129 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 140 | 166 | 27 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |
| `Action_None` | 212 | 215 | 4 | inferred_complete_timeline |
| `Action_None` | 217 | 226 | 10 | inferred_complete_timeline |
| `Action_None` | 228 | 231 | 4 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_None` | 249 | 256 | 8 | inferred_complete_timeline |
| `Action_None` | 259 | 288 | 30 | inferred_complete_timeline |
| `Action_None` | 290 | 299 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 11–128
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 70 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 115 | 43 | inferred_complete_timeline |
| `Action_DownBlock` | 116 | 128 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 11–146
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 115 | 105 | inferred_complete_timeline |
| `Action_DownBlock` | 116 | 146 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 11–200
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 115 | 105 | inferred_complete_timeline |
| `Action_DownBlock` | 116 | 148 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 156 | 181 | 26 | inferred_complete_timeline |
| `Action_None` | 182 | 200 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 11–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 204 | 194 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 299 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 11–299
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 69 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 140 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 153 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 157 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 299 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 11–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 196 | 186 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 230 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 299 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 11–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 48 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 132 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 245 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 299 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 11–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 185 | 175 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 205 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 299 | 93 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 11–265 | 252 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 60–299 | 167 | 4 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 63–299 | 237 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 116–200 | 85 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 137–299 | 104 | 6 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 165–170 | 6 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 166–258 | 93 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 195–299 | 101 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 222–236 | 15 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 227–298 | 68 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 239–299 | 61 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 241–299 | 58 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 258–299 | 35 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | 11 | 94 | 52 | 61.9% | 17–31, 60–76 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 59 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [11-184] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-265] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-204] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [116-129] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [140-166] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-226] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-231] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-256] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-288] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [116-148] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-196] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-230] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-69] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-140] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-153] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-299] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-185] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-205] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-70] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [116-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-172] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-183] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-48] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-132] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-245] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [116-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-46] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-167] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-240] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-264] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-134] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-189] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-214] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-139] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-155] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-219] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-170] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-258] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-233] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-236] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-243] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-298] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-253] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-277] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-287] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>
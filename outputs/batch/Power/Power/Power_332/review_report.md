# Play-Annotation-Generator Annotation Review — Power_332

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_332`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 0
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 4 | START | 4 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 4 | START | 4 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 4 | START | 10 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 4 | START | 64 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 4 | START | 4 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 4 | START | 4 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 4 | START | 4 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 4 | START | 4 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `12` | 129 | START | 129 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `2` | `2` | 129 | START | 129 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `6` | `6` | 129 | START | 129 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `4` | `4` | 129 | START | 129 | 131 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 4–157
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 157 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 64–299
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 64 | 216 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 270 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 299 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 299 | 296 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 10–160
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 160 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 4–160
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 128 | 125 | inferred_complete_timeline |
| `Action_PullBlock` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 142 | 148 | 7 | inferred_complete_timeline |
| `Action_PullBlock` | 156 | 160 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 128 | 125 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 166 | 181 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 190 | 230 | 41 | inferred_complete_timeline |
| `Action_None` | 231 | 299 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 128 | 125 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 154 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 194 | 228 | 35 | inferred_complete_timeline |
| `Action_None` | 242 | 264 | 23 | inferred_complete_timeline |
| `Action_None` | 280 | 292 | 13 | inferred_complete_timeline |
| `Action_None` | 295 | 299 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 4–226
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 128 | 125 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 136 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 154 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 157 | 171 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 173 | 226 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 123–299
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 123 | 167 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 299 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 199 | 196 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 274 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 293 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 299 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 4–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 194 | 191 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 232 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 4–291
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 202 | 199 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 217 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 226 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 271 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 291 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 173 | 170 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 205 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 299 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 4–158
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 152 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 158 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 185 | 182 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 222 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 290 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 4–26 | 23 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 136–299 | 158 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 157–192 | 36 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 159–280 | 111 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 174–240 | 67 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 177–299 | 42 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 179–299 | 108 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 184–299 | 114 | 3 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 204–299 | 96 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 223–299 | 77 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 241–299 | 59 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 245–299 | 55 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 253–299 | 46 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 256–298 | 32 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 262–263 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `4` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '2' (RG) duration 102 frames exceeds threshold 90 frames [start=129, end=230].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '6' (RT) duration 98 frames exceeds threshold 90 frames [start=129, end=226].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (C) duration 102 frames exceeds threshold 90 frames [start=129, end=230].
- ⚠️ Action 'Action_PreSnap' range [4-199] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-274] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-293] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [129-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [158-160] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [194-228] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-264] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-292] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-185] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-290] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [129-131] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [142-148] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [156-160] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-152] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-158] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [129-136] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [144-154] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [157-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [173-226] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-202] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-217] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-226] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-271] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-291] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-26] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-157] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-173] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-205] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-299] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-232] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-239] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [129-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [166-181] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [190-230] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-160] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-216] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-270] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-140] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-192] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-228] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-280] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-240] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-192] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-216] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-278] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-257] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-273] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-264] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-280] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-298] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-263] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>
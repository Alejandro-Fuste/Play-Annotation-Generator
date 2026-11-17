# Play-Annotation-Generator Annotation Review — Power_208

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_208`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 21
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 0
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 16 | START | 16 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 16 | START | 16 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 16 | START | 16 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 16 | START | 16 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 16 | START | 16 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 16 | START | 16 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 16 | START | 16 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 16 | START | 16 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `3` | `3` | 119 | START | 121 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `7` | `7` | 119 | START | 119 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `8` | `8` | 119 | START | 119 | 119 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 16–142
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 142 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 16–198
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 137 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 146 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 163 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 198 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 16–239
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 92 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 108 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 134 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 157 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 162 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 194 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 16–239
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 92 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 108 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 124 | 127 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 131 | 143 | 13 | inferred_complete_timeline |
| `Action_None` | 180 | 187 | 8 | inferred_complete_timeline |
| `Action_None` | 215 | 217 | 3 | inferred_complete_timeline |
| `Action_None` | 222 | 223 | 2 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |
| `Action_None` | 233 | 239 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 16–142
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 118 | 103 | inferred_complete_timeline |
| `Action_DownBlock` | 119 | 121 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 140 | 142 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 16–163
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 23 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 62 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 90 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 110 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 121 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 150 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 163 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 16–224
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 118 | 103 | inferred_complete_timeline |
| `Action_PullBlock` | 119 | 119 | 1 | inferred_complete_timeline |
| `Action_PullBlock` | 124 | 126 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 155 | 168 | 14 | inferred_complete_timeline |
| `Action_None` | 169 | 224 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 16–239
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 150 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 163 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 170 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 180 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 198 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 211 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 233 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 16–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 188 | 173 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 239 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 16–163
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 44 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 52 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 129 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 133 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 147 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 156 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 163 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 16–239
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 58 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 239 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 16–217
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 89 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 155 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 168 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 182 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 211 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 217 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 16–187
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 183 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 187 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 16–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 239 | 224 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 153–238 | 75 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 160–239 | 64 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 166–235 | 52 | 7 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 210–239 | 21 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 221–239 | 19 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 223–239 | 17 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 81 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [16-239] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-58] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-188] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-92] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-108] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [121-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [124-127] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [131-143] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-239] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-108] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-111] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-134] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-157] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-162] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-194] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-89] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-155] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-168] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-182] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-211] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-217] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-183] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-187] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [119-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [123-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [140-142] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' for track '8' starts at frame 119, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PullBlock' range [119-119] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [124-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-224] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-137] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-146] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-163] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-198] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-142] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-163] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-170] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-198] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-211] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-233] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-23] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-62] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-110] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-150] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-163] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-44] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-52] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-129] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-147] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-156] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-163] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-209] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-234] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-238] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-218] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-168] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-196] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-206] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-217] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-232] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-214] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-232] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-239] for track '17' has 2 frames without a visible bounding box.
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

</details>
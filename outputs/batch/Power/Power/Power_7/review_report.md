# Play-Annotation-Generator Annotation Review — Power_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_7`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 0
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 21 | START | 27 | 220 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 21 | START | 27 | 223 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 21 | START | 27 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 21 | START | 27 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 21 | START | 27 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 21 | START | 27 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 21 | START | 27 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 21 | START | 27 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 21 | START | 27 | 299 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `13` | 102 | START | 102 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `17` | `17` | 102 | START | 102 | 103 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 27–223
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 223 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 27–299
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 299 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 27–299
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 220 | 194 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 286 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 299 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 27–275
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 275 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 27–299
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 299 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 27–299
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 105 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 136 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 299 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 27–299
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 101 | 75 | inferred_complete_timeline |
| `Action_DownBlock` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 109 | 135 | 27 | inferred_complete_timeline |
| `Action_None` | 136 | 145 | 10 | inferred_complete_timeline |
| `Action_None` | 149 | 299 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 27–299
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 93 | 67 | inferred_complete_timeline |
| `Action_PullBlock` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 111 | 135 | 25 | inferred_complete_timeline |
| `Action_None` | 136 | 160 | 25 | inferred_complete_timeline |
| `Action_None` | 162 | 299 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 27–299
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 92 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 107 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 193 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 239 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 260 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 299 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 27–90
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 30 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 77 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 90 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 27–299
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 125 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 263 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 271 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 278 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 299 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 59–299
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 76 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 141 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 165 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 253 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 299 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 49–299
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 49 | 94 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 299 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 27–299
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 189 | 163 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 299 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 27–234
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 234 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 27–226
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 217 | 191 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 226 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 27–299
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 174 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 299 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 27–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 244 | 218 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 299 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 27–151
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 126 | 100 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 151 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 27–299
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 299 | 273 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 113–299 | 184 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 116–122 | 7 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 117–299 | 179 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 123–198 | 76 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 147–149 | 3 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 160–208 | 49 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 163–299 | 137 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 185–261 | 25 | 4 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 186–191 | 6 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 197–203 | 7 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 198–275 | 55 | 6 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 239–299 | 61 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 255–273 | 19 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 284–297 | 11 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 290–299 | 10 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 297–298 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 70 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [27-220] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-286] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-217] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-226] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-275] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-244] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-174] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-234] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-126] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-151] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-189] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-223] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-263] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-271] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-278] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [102-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [109-135] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-136] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-140] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-92] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-107] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-193] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-260] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-77] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-90] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-93] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [102-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-94] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-107] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-165] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-253] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-139] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-145] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-122] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-198] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-149] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-208] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-189] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-199] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-261] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-191] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-203] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-208] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-221] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-228] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-247] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-258] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-275] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-273] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-285] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-297] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-298] for track '35' has 1 frames without a visible bounding box.
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

</details>
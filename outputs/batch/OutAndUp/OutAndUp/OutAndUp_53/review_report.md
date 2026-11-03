# Play-Annotation-Generator Annotation Review — OutAndUp_53

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_53`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 269
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `21` |
| ✅ EXACT | `Action_SellOut` | WR3 | offense | `6` | `6` |
| ✅ EXACT | `Action_RunGoRoute` | WR3 | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 25 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `9` | 26 | START | 26 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `11` | `11` | 29 | START | 29 | 250 |
| ✅ EXACT | `Action_PassBlock` | RG | `14` | `14` | 29 | START | 29 | 250 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `7` | `7` | 29 | START | 29 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `8` | `8` | 29 | START | 29 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `9` | `9` | 29 | START | 42 | 161 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `21` | 41 | END | 26 | 41 |
| ✅ EXACT | `Action_SellOut` | WR3 | `6` | `6` | 74 | START | 74 | 113 |
| ✅ EXACT | `Action_RunGoRoute` | WR3 | `6` | `6` | 114 | START | 114 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | `21` | `21` | 134 | START | 134 | 135 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 26 | 41 | 16 | inferred_complete_timeline |
| `Action_None` | 42 | 133 | 92 | inferred_complete_timeline |
| `Action_ThrowPass` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_ThrowPass` | 138 | 145 | 8 | inferred_complete_timeline |
| `Action_None` | 146 | 150 | 5 | inferred_complete_timeline |
| `Action_None` | 152 | 191 | 40 | inferred_complete_timeline |
| `Action_None` | 193 | 241 | 49 | inferred_complete_timeline |
| `Action_None` | 244 | 250 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 135 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 269 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 193 | 256 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SellOut` | 74 | 113 | 40 | inferred_complete_timeline |
| `Action_RunGoRoute` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 269 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 118 | 90 | inferred_complete_timeline |
| `Action_PassBlock` | 121 | 241 | 121 | inferred_complete_timeline |
| `Action_PassBlock` | 250 | 252 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 250 | 222 | inferred_complete_timeline |
| `Action_PassBlock` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_BallSnap` | 26 | 41 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 161 | 120 | inferred_complete_timeline |
| `Action_PassBlock` | 163 | 191 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 193 | 258 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 250 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 114 | 86 | inferred_complete_timeline |
| `Action_PassBlock` | 116 | 241 | 126 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 129 | 104 | inferred_complete_timeline |
| `Action_None` | 131 | 150 | 20 | inferred_complete_timeline |
| `Action_None` | 153 | 168 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 87 | 62 | inferred_complete_timeline |
| `Action_None` | 93 | 190 | 98 | inferred_complete_timeline |
| `Action_None` | 193 | 241 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 176 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 267 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 269 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 269 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 241 | 216 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 269 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 269 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 226 | 201 | inferred_complete_timeline |
| `Action_None` | 233 | 269 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 269 | 244 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 162–234 | 73 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 175–241 | 67 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 180–256 | 67 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 186–234 | 45 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 220–246 | 27 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 232–260 | 20 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 242–258 | 17 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 242–244 | 3 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 242–267 | 26 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 244–247 | 4 | 1 | Undefined position; Undefined team |
| `32` | `51` | Position_Unknown | Team_Unknown | 245–247 | 3 | 1 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 245–250 | 6 | 1 | Undefined position; Undefined team |
| `34` | `54` | Position_Unknown | Team_Unknown | 246–252 | 7 | 1 | Undefined position; Undefined team |
| `35` | `57` | Position_Unknown | Team_Unknown | 249–250 | 2 | 1 | Undefined position; Undefined team |
| `36` | `59` | Position_Unknown | Team_Unknown | 251–255 | 5 | 1 | Undefined position; Undefined team |
| `37` | `64` | Position_Unknown | Team_Unknown | 259–269 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ThrowPass` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `19` (actor_track_id `19`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [26–41], lower_priority='Action_PassBlock' annotated_start=29, effective_Action_PassBlock_start=42.
- ⚠️ Action 'Action_None' range [26-87] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-190] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-241] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-129] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-168] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-176] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-190] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-256] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [114-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-114] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [116-241] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [121-241] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [250-252] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [163-191] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [193-258] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-267] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-250] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-241] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-250] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-226] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [134-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [138-145] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-191] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-241] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-250] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-234] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-241] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-241] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-256] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-221] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-246] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-241] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-260] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-258] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-267] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-250] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-252] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-255] for track '36' has 1 frames without a visible bounding box.
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

</details>
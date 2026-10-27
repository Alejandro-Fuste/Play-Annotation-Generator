# Play-Annotation-Generator Annotation Review — Counter_245

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_245`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `12` | `11` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `18` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 72 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `20` | `19` | 73 | START | 73 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `15` | `14` | 75 | START | 75 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `21` | `20` | 75 | START | 75 | 81 |
| ✅ EXACT | `Action_DownBlock` | RT | `22` | `21` | 75 | START | 75 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `19` | `18` | 76 | START | 76 | 94 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `12` | `11` | 76 | START | 76 | 148 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 84 | END | 73 | 84 |
| ✅ EXACT | `Action_BallCarry` | QB | `17` | `16` | 108 | START | 108 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 148 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_SnapReceive` | 73 | 84 | 12 | inferred_complete_timeline |
| `Action_None` | 85 | 107 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 108 | 269 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 259 | 187 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_None` | 264 | 265 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 269 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 162 | 90 | inferred_complete_timeline |
| `Action_None` | 165 | 269 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 245 | 173 | inferred_complete_timeline |
| `Action_None` | 252 | 269 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 269 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 76 | 148 | 73 | inferred_complete_timeline |
| `Action_None` | 149 | 269 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PullBlock` | 76 | 94 | 19 | inferred_complete_timeline |
| `Action_PullBlock` | 96 | 148 | 53 | inferred_complete_timeline |
| `Action_None` | 149 | 269 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_DownBlock` | 75 | 81 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 93 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_DownBlock` | 75 | 126 | 52 | inferred_complete_timeline |
| `Action_DownBlock` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 231 | 80 | inferred_complete_timeline |
| `Action_None` | 241 | 269 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_DownBlock` | 75 | 148 | 74 | inferred_complete_timeline |
| `Action_None` | 149 | 213 | 65 | inferred_complete_timeline |
| `Action_None` | 218 | 269 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 193 | 121 | inferred_complete_timeline |
| `Action_None` | 198 | 269 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 269 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_BallSnap` | 73 | 84 | 12 | inferred_complete_timeline |
| `Action_None` | 85 | 90 | 6 | inferred_complete_timeline |
| `Action_None` | 94 | 116 | 23 | inferred_complete_timeline |
| `Action_None` | 118 | 122 | 5 | inferred_complete_timeline |
| `Action_None` | 126 | 140 | 15 | inferred_complete_timeline |
| `Action_None` | 142 | 269 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 106 | 34 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 202 | 130 | inferred_complete_timeline |
| `Action_None` | 204 | 269 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 269 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 269 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 141 | 69 | inferred_complete_timeline |
| `Action_None` | 144 | 151 | 8 | inferred_complete_timeline |
| `Action_None` | 153 | 165 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 183 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 269 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 264 | 192 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 73–75 | 3 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 117–269 | 152 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 138–142 | 5 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 164–168 | 5 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 169–266 | 78 | 5 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 172–269 | 98 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 197–200 | 4 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 210–269 | 60 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 211–218 | 8 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 260–261 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 45 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [73-245] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-193] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-259] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-106] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-202] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-151] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-165] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-264] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [75-126] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [135-136] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-231] for track '14' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [76-94] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [96-148] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-116] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-122] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-140] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [75-81] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [83-85] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [88-93] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-213] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-141] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-168] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-178] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-215] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-261] for track '26' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-218] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '32' has 1 frames without a visible bounding box.
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

</details>
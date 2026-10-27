# Play-Annotation-Generator Annotation Review — Counter_15

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_15`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 131
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 70 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 61 | START | 61 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `10` | `9` | 71 | START | 71 | 92 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `18` | `17` | 71 | START | 83 | 145 |
| ✅ EXACT | `Action_DownBlock` | RG | `21` | `20` | 71 | START | 71 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `19` | `18` | 71 | START | 71 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `8` | `7` | 71 | START | 71 | 117 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 82 | END | 61 | 82 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `14` | 96 | START | 96 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `22` | `21` | 112 | START | 112 | 121 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 145 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_SnapReceive` | 61 | 82 | 22 | inferred_complete_timeline |
| `Action_None` | 83 | 95 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 96 | 111 | 16 | inferred_complete_timeline |
| `Action_None` | 112 | 269 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 111 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 112 | 121 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 123 | 138 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 269 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 269 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 71 | 117 | 47 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 121 | 145 | 25 | inferred_complete_timeline |
| `Action_None` | 146 | 208 | 63 | inferred_complete_timeline |
| `Action_None` | 211 | 237 | 27 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 199 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PullBlock` | 71 | 105 | 35 | inferred_complete_timeline |
| `Action_PullBlock` | 109 | 142 | 34 | inferred_complete_timeline |
| `Action_None` | 146 | 269 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_BallSnap` | 61 | 82 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 83 | 145 | 63 | inferred_complete_timeline |
| `Action_None` | 146 | 149 | 4 | inferred_complete_timeline |
| `Action_None` | 153 | 156 | 4 | inferred_complete_timeline |
| `Action_None` | 169 | 256 | 88 | inferred_complete_timeline |
| `Action_None` | 261 | 267 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_DownBlock` | 71 | 145 | 75 | inferred_complete_timeline |
| `Action_None` | 146 | 173 | 28 | inferred_complete_timeline |
| `Action_None` | 176 | 258 | 83 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_DownBlock` | 71 | 92 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 96 | 145 | 50 | inferred_complete_timeline |
| `Action_None` | 146 | 162 | 17 | inferred_complete_timeline |
| `Action_None` | 165 | 170 | 6 | inferred_complete_timeline |
| `Action_None` | 181 | 205 | 25 | inferred_complete_timeline |
| `Action_None` | 207 | 212 | 6 | inferred_complete_timeline |
| `Action_None` | 214 | 269 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 105 | 45 | inferred_complete_timeline |
| `Action_None` | 107 | 126 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 249 | 189 | inferred_complete_timeline |
| `Action_None` | 251 | 269 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 123 | 63 | inferred_complete_timeline |
| `Action_None` | 129 | 156 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 98 | 38 | inferred_complete_timeline |
| `Action_None` | 109 | 119 | 11 | inferred_complete_timeline |
| `Action_None` | 142 | 208 | 67 | inferred_complete_timeline |
| `Action_None` | 211 | 240 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 160 | 100 | inferred_complete_timeline |
| `Action_None` | 204 | 207 | 4 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 266 | 38 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 169 | 109 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 184 | 190 | 7 | inferred_complete_timeline |
| `Action_None` | 201 | 206 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 195 | 135 | inferred_complete_timeline |
| `Action_None` | 198 | 212 | 15 | inferred_complete_timeline |
| `Action_None` | 214 | 269 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 171 | 111 | inferred_complete_timeline |
| `Action_None` | 173 | 269 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 220 | 160 | inferred_complete_timeline |
| `Action_None` | 222 | 269 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 269 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 136 | 76 | inferred_complete_timeline |
| `Action_None` | 139 | 174 | 36 | inferred_complete_timeline |
| `Action_None` | 178 | 181 | 4 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–218 | 219 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 133–164 | 32 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 144–246 | 43 | 5 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 144–163 | 19 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 170–171 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 177–269 | 81 | 7 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 180–249 | 64 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 188–253 | 42 | 8 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 193–269 | 71 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 195–265 | 49 | 9 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 225–269 | 45 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `18` (C): Annotated start 71 != Inferred start 83
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 92 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [61–82], lower_priority='Action_DownBlock' annotated_start=71, effective_Action_DownBlock_start=83.
- ⚠️ Action 'Action_None' range [61-218] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-249] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-136] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-174] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-123] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-156] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [71-117] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-208] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-237] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [71-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-162] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-170] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-205] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-160] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-266] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-169] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-190] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-195] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-212] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-269] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-98] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-208] for track '15' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-240] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-126] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-256] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-267] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [71-105] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [109-142] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-199] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [71-145] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-173] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-258] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [123-138] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-164] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-230] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-246] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-160] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-207] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-226] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-253] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-239] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-240] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-241] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-205] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-261] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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
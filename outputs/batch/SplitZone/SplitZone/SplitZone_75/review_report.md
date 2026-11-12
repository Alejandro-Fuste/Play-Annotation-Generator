# Play-Annotation-Generator Annotation Review — SplitZone_75

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_75`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `17` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 108 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 106 | START | 106 | 119 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `10` | `10` | 109 | START | 109 | 196 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `12` | `12` | 109 | START | 109 | 204 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `14` | `14` | 109 | START | 109 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `21` | 109 | START | 123 | 133 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `9` | `9` | 109 | START | 109 | 204 |
| ✅ EXACT | `Action_SplitBlock` | TE | `2` | `2` | 114 | START | 114 | 161 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 121 | END | 106 | 121 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `18` | 125 | START | 125 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `17` | `17` | 136 | START | 136 | 173 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 204 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_SnapReceive` | 106 | 121 | 16 | inferred_complete_timeline |
| `Action_None` | 122 | 124 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 125 | 135 | 11 | inferred_complete_timeline |
| `Action_None` | 136 | 294 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_BallCarry` | 136 | 173 | 38 | inferred_complete_timeline |
| `Action_BallCarry` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 184 | 299 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 187 | 82 | inferred_complete_timeline |
| `Action_None` | 189 | 299 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 299 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 299 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_SplitBlock` | 114 | 161 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 204 | 96 | inferred_complete_timeline |
| `Action_None` | 205 | 299 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 196 | 88 | inferred_complete_timeline |
| `Action_None` | 205 | 208 | 4 | inferred_complete_timeline |
| `Action_None` | 215 | 223 | 9 | inferred_complete_timeline |
| `Action_None` | 225 | 227 | 3 | inferred_complete_timeline |
| `Action_None` | 231 | 299 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_BallSnap` | 106 | 119 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 133 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 153 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 167 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 204 | 35 | inferred_complete_timeline |
| `Action_None` | 205 | 299 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 151 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 158 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 204 | 96 | inferred_complete_timeline |
| `Action_None` | 205 | 299 | 95 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 214 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 195 | 90 | inferred_complete_timeline |
| `Action_None` | 205 | 242 | 38 | inferred_complete_timeline |
| `Action_None` | 249 | 253 | 5 | inferred_complete_timeline |
| `Action_None` | 256 | 299 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 137 | 32 | inferred_complete_timeline |
| `Action_None` | 146 | 278 | 133 | inferred_complete_timeline |
| `Action_None` | 280 | 299 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 133 | 28 | inferred_complete_timeline |
| `Action_None` | 136 | 185 | 50 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 204 | 14 | inferred_complete_timeline |
| `Action_None` | 217 | 221 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 178 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 186 | 81 | inferred_complete_timeline |
| `Action_None` | 193 | 195 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 184 | 79 | inferred_complete_timeline |
| `Action_None` | 187 | 189 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 299 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 299 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 244 | 139 | inferred_complete_timeline |
| `Action_None` | 252 | 255 | 4 | inferred_complete_timeline |
| `Action_None` | 257 | 299 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 260 | 155 | inferred_complete_timeline |
| `Action_None` | 264 | 267 | 4 | inferred_complete_timeline |
| `Action_None` | 272 | 291 | 20 | inferred_complete_timeline |
| `Action_None` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 131–299 | 169 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 185–299 | 102 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 188–299 | 105 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 189–193 | 5 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 202–299 | 98 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 202–299 | 96 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 219–299 | 73 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 220–273 | 52 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 266–268 | 3 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 285–297 | 13 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 287–289 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 96 frames exceeds threshold 90 frames [start=109, end=204].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (LG) duration 96 frames exceeds threshold 90 frames [start=109, end=204].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (LT) duration 96 frames exceeds threshold 90 frames [start=109, end=204].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (C) duration 96 frames exceeds threshold 90 frames [start=109, end=204].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [106–121], lower_priority='Action_ZoneBlock' annotated_start=109, effective_Action_ZoneBlock_start=122.
- ⚠️ Action 'Action_SplitBlock' range [114-161] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-195] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-242] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-187] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-204] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-196] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-223] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-133] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-185] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-204] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-214] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [157-158] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-184] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-244] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [136-173] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [181-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-294] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-260] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-291] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-137] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-278] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [106-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [149-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [157-167] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-202] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-209] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-222] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-228] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-299] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-269] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-297] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '32' has 1 frames without a visible bounding box.
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
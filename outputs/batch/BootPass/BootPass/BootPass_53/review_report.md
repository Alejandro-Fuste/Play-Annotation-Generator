# Play-Annotation-Generator Annotation Review — BootPass_53

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_53`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Comp.`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 78
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `17` | `17` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_FakeHandoff` | RB | offense | `5` | `5` |
| ✅ EXACT | `Action_BootAway` | RB | offense | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | SAF2 | defense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 59 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 35 | START | 35 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `15` | `15` | 44 | START | 54 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `17` | `17` | 44 | START | 44 | 48 |
| ✅ EXACT | `Action_RunBlock` | LG | `19` | `19` | 44 | START | 44 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `20` | `20` | 44 | START | 44 | 140 |
| ✅ EXACT | `Action_RunBlock` | LT | `21` | `21` | 44 | START | 44 | 203 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 53 | END | 35 | 53 |
| ✅ EXACT | `Action_FakeHandoff` | RB | `5` | `5` | 60 | START | 60 | 75 |
| ✅ EXACT | `Action_BootAway` | RB | `5` | `5` | 76 | START | 76 | 105 |
| ✅ EXACT | `Action_ThrowPass` | SAF2 | `12` | `12` | 153 | START | 153 | 164 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_SnapReceive` | 35 | 53 | 19 | inferred_complete_timeline |
| `Action_None` | 54 | 74 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_FakeHandoff` | 60 | 75 | 16 | inferred_complete_timeline |
| `Action_BootAway` | 76 | 105 | 30 | inferred_complete_timeline |
| `Action_None` | 106 | 195 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 82 | 48 | inferred_complete_timeline |
| `Action_None` | 84 | 189 | 106 | inferred_complete_timeline |
| `Action_None` | 193 | 195 | 3 | inferred_complete_timeline |
| `Action_None` | 197 | 200 | 4 | inferred_complete_timeline |
| `Action_None` | 206 | 231 | 26 | inferred_complete_timeline |
| `Action_None` | 235 | 237 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 205 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 239 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_RunBlock` | 44 | 203 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_RunBlock` | 44 | 206 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_BallSnap` | 35 | 53 | 19 | inferred_complete_timeline |
| `Action_RunBlock` | 54 | 137 | 84 | inferred_complete_timeline |
| `Action_RunBlock` | 143 | 150 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_RunBlock` | 44 | 48 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 56 | 61 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 64 | 98 | 35 | inferred_complete_timeline |
| `Action_RunBlock` | 104 | 123 | 20 | inferred_complete_timeline |
| `Action_RunBlock` | 129 | 131 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_RunBlock` | 44 | 140 | 97 | inferred_complete_timeline |
| `Action_RunBlock` | 142 | 197 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 145 | 111 | inferred_complete_timeline |
| `Action_None` | 150 | 162 | 13 | inferred_complete_timeline |
| `Action_None` | 164 | 196 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 111 | 77 | inferred_complete_timeline |
| `Action_None` | 113 | 116 | 4 | inferred_complete_timeline |
| `Action_None` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_None` | 126 | 132 | 7 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 202 | 168 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 182 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 221 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 204 | 170 | inferred_complete_timeline |
| `Action_None` | 207 | 239 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 239 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 189 | 155 | inferred_complete_timeline |
| `Action_None` | 205 | 230 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 227 | 193 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 227 | 193 | inferred_complete_timeline |
| `Action_None` | 229 | 239 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_ThrowPass` | 153 | 164 | 12 | inferred_complete_timeline |
| `Action_None` | 165 | 188 | 24 | inferred_complete_timeline |
| `Action_None` | 196 | 200 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–235 | 236 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 78–202 | 125 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 81–82 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 131–199 | 69 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 156–199 | 44 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 159–166 | 8 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 161–190 | 30 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 204–224 | 9 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 208–223 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `17` (6 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_SecureCatch' at frame 225 targets track ID '31', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 86: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [35–53], lower_priority='Action_RunBlock' annotated_start=44, effective_Action_RunBlock_start=54.
- ⚠️ Action 'Action_None' range [35-111] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-132] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-82] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-189] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-231] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-227] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-189] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-230] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [60-75] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-195] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-182] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-221] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-204] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-196] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-235] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-152] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-227] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [54-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [143-150] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-202] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [44-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [53-54] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [56-61] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [64-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [104-123] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [129-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-205] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [44-206] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [44-140] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [142-197] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [44-203] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-202] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-199] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-199] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-166] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-209] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-223] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>
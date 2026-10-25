# Play-Annotation-Generator Annotation Review — BootPass_98

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_98`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Comp.`
- **Result Frame:** 299
- **Player Tracks:** 24
- **Ball Tracks:** 1
- **Action Segments:** 53
- **Validation Warnings:** 48
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 9
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 33
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_RunFlatRoute` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_SecureCatch` | DT1 | defense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `14` | `14` | 101 | START | 101 | 112 |
| ✅ EXACT | `Action_RunBlock` | LG | `12` | `12` | 111 | START | 111 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `14` | `14` | 111 | START | 119 | 176 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `6` | `6` | 111 | START | 111 | 134 |
| ✅ EXACT | `Action_RunBlock` | RT | `7` | `7` | 111 | START | 111 | 190 |
| ✅ EXACT | `Action_RunBlock` | RG | `8` | `8` | 111 | START | 111 | 186 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 118 | END | 101 | 118 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `13` | `13` | 122 | START | 122 | 144 |
| ✅ EXACT | `Action_BootAway` | QB | `13` | `13` | 146 | START | 146 | 174 |
| ✅ EXACT | `Action_RunFlatRoute` | LT | `6` | `6` | 153 | START | 153 | 175 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 175 | START | 175 | 182 |
| ✅ EXACT | `Action_SecureCatch` | DT1 | `10` | `10` | 184 | START | 184 | 184 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_SnapReceive` | 101 | 118 | 18 | inferred_complete_timeline |
| `Action_None` | 119 | 121 | 3 | inferred_complete_timeline |
| `Action_FakeHandoff` | 122 | 144 | 23 | inferred_complete_timeline |
| `Action_BootAway` | 146 | 174 | 29 | inferred_complete_timeline |
| `Action_ThrowPass` | 175 | 182 | 8 | inferred_complete_timeline |
| `Action_None` | 183 | 201 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 180 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 168 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_RunBlock` | 111 | 134 | 24 | inferred_complete_timeline |
| `Action_RunBlock` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 148 | 152 | 5 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 153 | 175 | 23 | inferred_complete_timeline |
| `Action_None` | 176 | 299 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_RunBlock` | 111 | 178 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_BallSnap` | 101 | 112 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 114 | 118 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 119 | 176 | 58 | inferred_complete_timeline |
| `Action_RunBlock` | 179 | 182 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_RunBlock` | 111 | 186 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_RunBlock` | 111 | 190 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 174 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 215 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_SecureCatch` | 184 | 184 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 199 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 188 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 196 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 204 | 104 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 154–164 | 11 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 171–175 | 5 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 226–299 | 73 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 274–295 | 22 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 285–299 | 15 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 285–291 | 7 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 287–299 | 13 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 293–299 | 7 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | 28 | 51 | 12 | 50.0% | 30–31, 37, 42–50 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `6` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 28 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [101–118], lower_priority='Action_RunBlock' annotated_start=111, effective_Action_RunBlock_start=119.
- ⚠️ Action 'Action_None' range [101-188] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-196] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-180] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-215] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [111-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [138-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [144-145] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [111-190] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [111-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-204] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' for track '10' starts at frame 184, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_SecureCatch' range [184-184] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [111-178] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [122-144] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-201] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [101-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [119-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [179-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-299] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-295] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '21' has 1 frames without a visible bounding box.
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

</details>
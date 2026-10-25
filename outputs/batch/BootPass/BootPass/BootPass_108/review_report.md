# Play-Annotation-Generator Annotation Review — BootPass_108

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_108`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 66
- **Validation Warnings:** 78
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `8` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `1` | `1` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `3` | `3` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `7` | `7` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | DT2 | defense | `12` | `12` |
| ✅ EXACT | `Action_FakeHandoff` | DT2 | defense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | DT2 | defense | `12` | `12` |
| ✅ EXACT | `Action_RunFlatRoute` | TE | offense | `2` | `2` |
| ✅ EXACT | `Action_ThrowPass` | DT2 | defense | `12` | `12` |
| ✅ EXACT | `Action_SecureCatch` | RT | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `8` | 24 | START | 24 | 54 |
| ✅ EXACT | `Action_RunBlock` | RT | `1` | `1` | 47 | START | 47 | 185 |
| ✅ EXACT | `Action_RunBlock` | RG | `3` | `3` | 47 | START | 47 | 165 |
| ✅ EXACT | `Action_RunBlock` | LT | `5` | `5` | 47 | START | 47 | 174 |
| ✅ EXACT | `Action_RunBlock` | LG | `7` | `7` | 47 | START | 47 | 197 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `8` | `8` | 47 | START | 55 | 188 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | DT2 | `12` | `12` | 54 | END | 24 | 37 |
| ✅ EXACT | `Action_FakeHandoff` | DT2 | `12` | `12` | 64 | START | 64 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | DT2 | `12` | `12` | 86 | START | 86 | 89 |
| ✅ EXACT | `Action_RunFlatRoute` | TE | `2` | `2` | 94 | START | 94 | 141 |
| ✅ EXACT | `Action_ThrowPass` | DT2 | `12` | `12` | 141 | START | 141 | 152 |
| ✅ EXACT | `Action_SecureCatch` | RT | `1` | `1` | 186 | START | 186 | 207 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 210 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 148 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 94 | 141 | 48 | inferred_complete_timeline |
| `Action_None` | 142 | 210 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_RunBlock` | 47 | 174 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_RunBlock` | 47 | 197 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_BallSnap` | 24 | 54 | 31 | inferred_complete_timeline |
| `Action_RunBlock` | 55 | 188 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_RunBlock` | 47 | 165 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_RunBlock` | 47 | 185 | 139 | inferred_complete_timeline |
| `Action_SecureCatch` | 186 | 207 | 22 | inferred_complete_timeline |
| `Action_None` | 208 | 208 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 124 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 201 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_None` | 91 | 100 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 37 | 14 | inferred_complete_timeline |
| `Action_SnapReceive` | 43 | 49 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 54 | 54 | 1 | inferred_complete_timeline |
| `Action_None` | 55 | 63 | 9 | inferred_complete_timeline |
| `Action_FakeHandoff` | 64 | 85 | 22 | inferred_complete_timeline |
| `Action_BootAway` | 86 | 89 | 4 | inferred_complete_timeline |
| `Action_BootAway` | 93 | 106 | 14 | inferred_complete_timeline |
| `Action_BootAway` | 115 | 140 | 26 | inferred_complete_timeline |
| `Action_ThrowPass` | 141 | 152 | 12 | inferred_complete_timeline |
| `Action_None` | 153 | 184 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 175 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 161 | 138 | inferred_complete_timeline |
| `Action_None` | 163 | 198 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 4–210 | 207 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 69–210 | 142 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 93–94 | 2 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 93–169 | 76 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 119–164 | 46 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 135–210 | 76 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 144–167 | 24 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 156–180 | 18 | 2 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 160–175 | 8 | 2 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 173–210 | 38 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 176–177 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 178–210 | 33 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 181–210 | 30 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 187–210 | 15 | 4 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 191–192 | 2 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_RunBlock` for actor_track_id `8` (C): Annotated start 47 != Inferred start 55
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BootAway` and target `12` (3 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [24–54], lower_priority='Action_RunBlock' annotated_start=47, effective_Action_RunBlock_start=55.
- ⚠️ Action 'Action_None' range [24-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-198] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '1' starts at frame 208, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [208-208] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [47-165] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-148] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [47-174] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [47-197] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [55-188] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-87] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-124] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [24-37] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [43-49] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [86-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [93-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [115-140] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-184] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-201] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-169] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-164] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-165] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '29' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.

</details>
# Play-Annotation-Generator Annotation Review — BootPass_71

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_71`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Comp.`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 64
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_SecureCatch` | TE2 | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `16` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 206 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 77 | START | 77 | 83 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `14` | `14` | 83 | START | 84 | 227 |
| ✅ EXACT | `Action_RunBlock` | LT | `17` | `17` | 83 | START | 83 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `18` | `18` | 83 | START | 83 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `20` | `20` | 83 | START | 83 | 121 |
| ✅ EXACT | `Action_RunBlock` | LG | `21` | `21` | 83 | START | 83 | 220 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 83 | END | 77 | 83 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `19` | `19` | 110 | START | 110 | 122 |
| ✅ EXACT | `Action_BootAway` | QB | `19` | `19` | 123 | START | 123 | 163 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 166 | START | 166 | 177 |
| ✅ EXACT | `Action_SecureCatch` | TE2 | `4` | `4` | 207 | START | 207 | 226 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_SnapReceive` | 77 | 83 | 7 | inferred_complete_timeline |
| `Action_None` | 84 | 109 | 26 | inferred_complete_timeline |
| `Action_FakeHandoff` | 110 | 122 | 13 | inferred_complete_timeline |
| `Action_BootAway` | 123 | 163 | 41 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_ThrowPass` | 166 | 177 | 12 | inferred_complete_timeline |
| `Action_None` | 178 | 231 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 120 | 44 | inferred_complete_timeline |
| `Action_None` | 123 | 156 | 34 | inferred_complete_timeline |
| `Action_None` | 158 | 228 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 239 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 239 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 239 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_SecureCatch` | 207 | 226 | 20 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_RunBlock` | 83 | 113 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_RunBlock` | 83 | 220 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_BallSnap` | 77 | 83 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 84 | 227 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_RunBlock` | 83 | 100 | 18 | inferred_complete_timeline |
| `Action_RunBlock` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 105 | 114 | 10 | inferred_complete_timeline |
| `Action_RunBlock` | 119 | 167 | 49 | inferred_complete_timeline |
| `Action_RunBlock` | 173 | 226 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_RunBlock` | 83 | 121 | 39 | inferred_complete_timeline |
| `Action_RunBlock` | 123 | 237 | 115 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 113 | 37 | inferred_complete_timeline |
| `Action_None` | 117 | 144 | 28 | inferred_complete_timeline |
| `Action_None` | 149 | 169 | 21 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 113 | 37 | inferred_complete_timeline |
| `Action_None` | 115 | 239 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 118 | 42 | inferred_complete_timeline |
| `Action_None` | 128 | 142 | 15 | inferred_complete_timeline |
| `Action_None` | 144 | 231 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 134 | 58 | inferred_complete_timeline |
| `Action_None` | 140 | 151 | 12 | inferred_complete_timeline |
| `Action_None` | 163 | 169 | 7 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 205 | 18 | inferred_complete_timeline |
| `Action_None` | 207 | 237 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 239 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 187 | 111 | inferred_complete_timeline |
| `Action_None` | 191 | 239 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 123 | 47 | inferred_complete_timeline |
| `Action_None` | 138 | 150 | 13 | inferred_complete_timeline |
| `Action_None` | 161 | 239 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 239 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 239 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 141 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 239 | 163 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–116 | 115 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 159–239 | 81 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 166–221 | 45 | 4 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 178–232 | 34 | 5 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 187–204 | 18 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 195–205 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_RunBlock` for actor_track_id `14` (C): Annotated start 83 != Inferred start 84
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [77–83], lower_priority='Action_RunBlock' annotated_start=83, effective_Action_RunBlock_start=84.
- ⚠️ Action 'Action_None' range [77-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-156] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-228] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-187] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-206] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-118] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-142] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-231] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-113] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-113] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-239] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-134] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-151] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-169] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-205] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-237] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [84-227] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [83-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [83-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [102-103] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [105-114] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [119-167] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [173-226] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-231] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [83-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [123-237] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [83-220] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-108] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-116] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-180] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-194] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-221] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-201] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-217] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-229] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-204] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '27' has 1 frames without a visible bounding box.
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

</details>
# Play-Annotation-Generator Annotation Review — OutRoutes_71

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_71`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunOutRoute` | WR4 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_SecureCatch` | WR4 | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR4 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `1` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `20` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_PassBlock` | C | `15` | `15` | 5 | START | 5 | 239 |
| ✅ EXACT | `Action_PassBlock` | LT | `16` | `16` | 5 | START | 5 | 200 |
| ✅ EXACT | `Action_PassBlock` | RG | `17` | `17` | 5 | START | 5 | 239 |
| ✅ EXACT | `Action_PassBlock` | LG | `18` | `18` | 5 | START | 5 | 239 |
| ✅ EXACT | `Action_PassBlock` | RT | `9` | `9` | 5 | START | 5 | 239 |
| ✅ EXACT | `Action_RunOutRoute` | WR4 | `2` | `2` | 11 | START | 11 | 99 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 11 | END | 11 | 11 |
| ✅ EXACT | `Action_ThrowPass` | QB | `11` | `11` | 64 | START | 64 | 73 |
| ✅ EXACT | `Action_SecureCatch` | WR4 | `2` | `2` | 100 | START | 100 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR4 | `2` | `2` | 109 | START | 109 | 223 |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 11 | 1 | inferred_complete_timeline |
| `Action_None` | 12 | 63 | 52 | inferred_complete_timeline |
| `Action_ThrowPass` | 64 | 73 | 10 | inferred_complete_timeline |
| `Action_None` | 74 | 239 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_RunOutRoute` | 11 | 99 | 89 | inferred_complete_timeline |
| `Action_SecureCatch` | 100 | 108 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 109 | 223 | 115 | inferred_complete_timeline |
| `Action_BallCarry` | 225 | 227 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 200 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 239 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 239 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 239 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 239 | 235 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 102 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 116 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 239 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 153 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 239 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 110 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 206 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 126 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 64–239 | 175 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 88–90 | 3 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 107–162 | 25 | 4 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 116–117 | 2 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 143–144 | 2 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 172–208 | 29 | 3 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 174–175 | 2 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 189–239 | 51 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 190–205 | 15 | 2 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 190–191 | 2 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 194–238 | 28 | 5 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 197–239 | 38 | 2 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 208–209 | 2 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 212–217 | 6 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 218–222 | 5 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 222–239 | 18 | 1 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 50 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_BallCarry' range [109-223] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [225-227] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-153] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-126] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-102] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-191] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-215] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-239] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-110] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-206] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-67] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-239] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-90] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-113] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-148] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-162] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-117] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-165] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-196] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-203] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-175] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-192] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-205] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-206] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-217] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-227] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-238] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-227] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-239] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-209] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-217] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-222] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '40' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>
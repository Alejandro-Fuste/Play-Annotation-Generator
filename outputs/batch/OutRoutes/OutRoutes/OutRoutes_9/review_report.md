# Play-Annotation-Generator Annotation Review — OutRoutes_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_9`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `21` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `21` | `21` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_PassBlock` | RT | `16` | `16` | 6 | START | 6 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `17` | 6 | START | 6 | 13 |
| ✅ EXACT | `Action_PassBlock` | LT | `18` | `18` | 6 | START | 6 | 239 |
| ✅ EXACT | `Action_PassBlock` | LG | `19` | `19` | 6 | START | 6 | 75 |
| ✅ EXACT | `Action_PassBlock` | RG | `20` | `20` | 6 | START | 6 | 35 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `7` | `7` | 13 | START | 13 | 104 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `21` | 13 | END | 13 | 13 |
| ✅ EXACT | `Action_ThrowPass` | QB | `21` | `21` | 73 | START | 73 | 82 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `7` | `7` | 105 | START | 105 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `7` | `7` | 111 | START | 111 | 219 |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_SnapReceive` | 13 | 13 | 1 | inferred_complete_timeline |
| `Action_None` | 14 | 72 | 59 | inferred_complete_timeline |
| `Action_ThrowPass` | 73 | 82 | 10 | inferred_complete_timeline |
| `Action_None` | 83 | 239 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 85 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 90 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 113 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 127 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_RunOutRoute` | 13 | 104 | 92 | inferred_complete_timeline |
| `Action_SecureCatch` | 105 | 110 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 111 | 219 | 109 | inferred_complete_timeline |
| `Action_BallCarry` | 223 | 233 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 236 | 239 | 4 | inferred_complete_timeline |

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
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 239 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 75 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 13 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 24 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 113 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 120 | 239 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 35 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 239 | 234 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 150 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 158 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 239 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 239 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 45 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 124 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 239 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 239 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 109 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 193 | 86 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 11–58 | 41 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 42–43 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 50–58 | 9 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 71–83 | 11 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 83–84 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 84–87 | 4 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 90–98 | 9 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 102–141 | 34 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 103–108 | 6 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 105–196 | 91 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 113–125 | 8 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 121–138 | 7 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 122–123 | 2 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 128–131 | 4 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 134–143 | 9 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 139–239 | 88 | 3 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 151–193 | 43 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 155–239 | 82 | 2 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 177–239 | 63 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 178–190 | 8 | 3 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 211–239 | 28 | 2 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 221–229 | 7 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 71 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-86] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-219] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-224] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-193] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [111-219] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [223-233] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-109] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-152] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-90] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-113] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-127] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-124] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-13] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-24] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [80-113] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-75] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-35] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-20] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-34] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-54] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-58] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-58] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-79] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-87] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-98] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-104] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-141] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-108] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-192] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-196] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-114] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-125] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-125] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-138] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-123] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-131] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-139] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-143] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-160] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-173] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-193] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-207] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-239] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-181] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-187] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-222] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-239] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-223] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '44' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.

</details>
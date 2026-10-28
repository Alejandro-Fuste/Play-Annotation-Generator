# Play-Annotation-Generator Annotation Review — Draw_23

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_23`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Slide`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `7` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 34 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 32 | START | 32 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `16` | 35 | START | 48 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `18` | `17` | 35 | START | 35 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `18` | 35 | START | 35 | 62 |
| ✅ EXACT | `Action_PassBlock` | RT | `20` | `19` | 35 | START | 35 | 131 |
| ✅ EXACT | `Action_PassBlock` | LT | `9` | `8` | 35 | START | 35 | 131 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 47 | END | 32 | 47 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `5` | `4` | 50 | START | 50 | 73 |
| ✅ EXACT | `Action_BallCarry` | QB | `5` | `4` | 74 | START | 74 | 236 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 131 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_SnapReceive` | 32 | 47 | 16 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 50 | 73 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 74 | 236 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 158 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 140 | 109 | inferred_complete_timeline |
| `Action_None` | 144 | 196 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 131 | 97 | inferred_complete_timeline |
| `Action_None` | 132 | 223 | 92 | inferred_complete_timeline |
| `Action_None` | 227 | 236 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 62 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 68 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 47 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 99 | 52 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 153 | 7 | inferred_complete_timeline |
| `Action_None` | 155 | 170 | 16 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 109 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 131 | 97 | inferred_complete_timeline |
| `Action_None` | 132 | 135 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 63 | 32 | inferred_complete_timeline |
| `Action_None` | 84 | 239 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 68 | 37 | inferred_complete_timeline |
| `Action_None` | 76 | 124 | 49 | inferred_complete_timeline |
| `Action_None` | 126 | 203 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 120 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 210 | 179 | inferred_complete_timeline |
| `Action_None` | 212 | 224 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 101 | 70 | inferred_complete_timeline |
| `Action_None` | 112 | 165 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 215 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 83 | 52 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_None` | 100 | 149 | 50 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 100 | 69 | inferred_complete_timeline |
| `Action_None` | 117 | 239 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 157 | 126 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 66–239 | 165 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 119–191 | 73 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 126–127 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 148–219 | 70 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 167–216 | 43 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 189–239 | 51 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 192–215 | 17 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 196–211 | 16 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 222–239 | 18 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `21`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [32–47], lower_priority='Action_PassBlock' annotated_start=35, effective_Action_PassBlock_start=48.
- ⚠️ Action 'Action_None' range [32-158] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-140] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-196] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-83] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [74-236] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-239] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-68] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-203] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-131] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-223] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-236] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-215] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-165] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-120] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-224] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [48-99] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-153] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-170] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-62] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-68] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-157] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-83] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-239] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-191] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-219] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-176] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-184] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-216] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-211] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '30' has 1 frames without a visible bounding box.
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

</details>
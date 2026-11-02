# Play-Annotation-Generator Annotation Review — JetSweep_159

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_159`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 65
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR1 | offense | `20` | `19` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `20` |
| ✅ EXACT | `Action_Toss` | QB | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `20` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR1 | `20` | `19` | 31 | START | 31 | 39 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 63 | START | 63 | 75 |
| ✅ EXACT | `Action_LeadBlock` | RB | `18` | `17` | 65 | START | 65 | 129 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `13` | `12` | 65 | START | 65 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `15` | `14` | 65 | START | 65 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `15` | `14` | 65 | START | 65 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 65 | START | 65 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 65 | START | 65 | 75 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `20` | 76 | END | 63 | 76 |
| ✅ EXACT | `Action_Toss` | QB | `21` | `20` | 83 | START | 83 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `20` | `19` | 92 | START | 92 | 132 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 129 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_SnapReceive` | 63 | 76 | 14 | inferred_complete_timeline |
| `Action_None` | 77 | 82 | 6 | inferred_complete_timeline |
| `Action_Toss` | 83 | 91 | 9 | inferred_complete_timeline |
| `Action_None` | 92 | 239 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_LeadBlock` | 65 | 129 | 65 | inferred_complete_timeline |
| `Action_None` | 130 | 184 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_JetMotion` | 31 | 39 | 9 | inferred_complete_timeline |
| `Action_JetMotion` | 42 | 52 | 11 | inferred_complete_timeline |
| `Action_JetMotion` | 54 | 58 | 5 | inferred_complete_timeline |
| `Action_JetMotion` | 60 | 91 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 92 | 132 | 41 | inferred_complete_timeline |
| `Action_BallCarry` | 136 | 215 | 80 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 239 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 225 | 163 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 239 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 129 | 65 | inferred_complete_timeline |
| `Action_None` | 130 | 239 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 82 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 98 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 120 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_BallSnap` | 63 | 75 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 75 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 129 | 53 | inferred_complete_timeline |
| `Action_None` | 130 | 213 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 113 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 129 | 4 | inferred_complete_timeline |
| `Action_None` | 130 | 239 | 110 | inferred_complete_timeline |

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
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 239 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 105 | 43 | inferred_complete_timeline |
| `Action_None` | 108 | 212 | 105 | inferred_complete_timeline |
| `Action_None` | 218 | 220 | 3 | inferred_complete_timeline |
| `Action_None` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 231 | 169 | inferred_complete_timeline |
| `Action_None` | 233 | 239 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 107 | 45 | inferred_complete_timeline |
| `Action_None` | 135 | 239 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 239 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 239 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 157 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 213 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 212 | 150 | inferred_complete_timeline |
| `Action_None` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_None` | 218 | 222 | 5 | inferred_complete_timeline |
| `Action_None` | 227 | 229 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 239 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 206 | 144 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 98–239 | 117 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 116–117 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 120–121 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 125–239 | 115 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 158–177 | 20 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 185–239 | 55 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 185–239 | 43 | 3 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 228–233 | 6 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 234–239 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [63–75], lower_priority='Action_ZoneBlock' annotated_start=65, effective_Action_ZoneBlock_start=76.
- ⚠️ Action 'Action_None' range [63-225] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-213] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-105] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-212] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-157] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-212] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-107] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [63-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-113] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-231] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [65-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-184] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-98] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [31-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [42-52] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [54-58] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [92-132] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [136-215] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-75] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-213] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-127] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-214] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-233] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '31' has 1 frames without a visible bounding box.
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
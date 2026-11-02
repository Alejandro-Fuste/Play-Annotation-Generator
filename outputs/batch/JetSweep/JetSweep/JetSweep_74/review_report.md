# Play-Annotation-Generator Annotation Review — JetSweep_74

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_74`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `2` | `1` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE2 | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `1` | `0` |
| ✅ EXACT | `Action_Toss` | QB | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `15` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 87 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `2` | `1` | 49 | START | 49 | 115 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 88 | START | 88 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE2 | `15` | `14` | 89 | START | 89 | 208 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `14` | `13` | 89 | START | 89 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `16` | 89 | START | 102 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `19` | 89 | START | 89 | 169 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `20` | 89 | START | 89 | 169 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `2` | 89 | START | 89 | 169 |
| ✅ EXACT | `Action_SnapReceive` | QB | `1` | `0` | 101 | END | 88 | 101 |
| ✅ EXACT | `Action_Toss` | QB | `1` | `0` | 107 | START | 107 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `2` | `1` | 116 | START | 116 | 292 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 169 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_SnapReceive` | 88 | 101 | 14 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_Toss` | 107 | 115 | 9 | inferred_complete_timeline |
| `Action_None` | 116 | 329 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 329 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_JetMotion` | 49 | 115 | 67 | inferred_complete_timeline |
| `Action_BallCarry` | 116 | 292 | 177 | inferred_complete_timeline |
| `Action_BallCarry` | 297 | 329 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 167 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 328 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_SealBlock` | 89 | 208 | 120 | inferred_complete_timeline |
| `Action_SealBlock` | 211 | 329 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 169 | 81 | inferred_complete_timeline |
| `Action_None` | 170 | 329 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 169 | 81 | inferred_complete_timeline |
| `Action_None` | 170 | 329 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_BallSnap` | 88 | 101 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 105 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 123 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 145 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 151 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 169 | 81 | inferred_complete_timeline |
| `Action_None` | 170 | 329 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 169 | 81 | inferred_complete_timeline |
| `Action_None` | 170 | 329 | 160 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 133 | 46 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 131 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 107 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 106 | 19 | inferred_complete_timeline |
| `Action_None` | 109 | 329 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 140 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 329 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 329 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 213 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 138 | 51 | inferred_complete_timeline |
| `Action_None` | 145 | 172 | 28 | inferred_complete_timeline |
| `Action_None` | 174 | 329 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 329 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 230 | 143 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `29` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 126–329 | 202 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 129–297 | 166 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 132–329 | 188 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 153–329 | 172 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 161–329 | 159 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 195–329 | 135 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 226–236 | 9 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 235–325 | 78 | 5 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 235–278 | 23 | 5 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 239–329 | 91 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 250–288 | 32 | 4 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 294–296 | 3 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 299–301 | 3 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 311–313 | 3 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 324–329 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SealBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [88–101], lower_priority='Action_ZoneBlock' annotated_start=89, effective_Action_ZoneBlock_start=102.
- ⚠️ Action 'Action_BallCarry' range [116-292] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [297-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-167] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-213] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-138] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-230] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-107] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [89-208] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-329] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [88-101] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [107-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [150-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-328] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-131] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-285] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-297] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-139] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-160] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-244] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-278] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-297] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-313] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-247] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-259] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-271] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-329] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-278] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '37' has 1 frames without a visible bounding box.
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

</details>
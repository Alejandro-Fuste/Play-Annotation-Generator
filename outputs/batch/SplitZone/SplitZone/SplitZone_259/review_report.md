# Play-Annotation-Generator Annotation Review — SplitZone_259

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_259`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `14` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 9 | START | 10 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 9 | START | 10 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 9 | START | 10 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 9 | START | 10 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 9 | START | 10 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 9 | START | 10 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 9 | START | 10 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 9 | START | 10 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 9 | START | 10 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 9 | START | 10 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 9 | START | 10 | 121 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 112 | START | 112 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `13` | `13` | 115 | START | 115 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `15` | 115 | START | 128 | 131 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `18` | `18` | 115 | START | 115 | 204 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `19` | `19` | 115 | START | 115 | 150 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `21` | `21` | 115 | START | 115 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `9` | `9` | 122 | START | 122 | 194 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 127 | END | 112 | 127 |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `20` | 131 | START | 131 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `14` | `14` | 140 | START | 140 | 372 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 210 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 10–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 111 | 102 | inferred_complete_timeline |
| `Action_SnapReceive` | 112 | 127 | 16 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 131 | 139 | 9 | inferred_complete_timeline |
| `Action_None` | 140 | 389 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 10–389
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 139 | 130 | inferred_complete_timeline |
| `Action_BallCarry` | 140 | 372 | 233 | inferred_complete_timeline |
| `Action_BallCarry` | 381 | 389 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 10–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 111 | 102 | inferred_complete_timeline |
| `Action_None` | 112 | 290 | 179 | inferred_complete_timeline |
| `Action_None` | 292 | 389 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 10–382
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 111 | 102 | inferred_complete_timeline |
| `Action_None` | 112 | 372 | 261 | inferred_complete_timeline |
| `Action_None` | 374 | 376 | 3 | inferred_complete_timeline |
| `Action_None` | 381 | 382 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 10–389
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 111 | 102 | inferred_complete_timeline |
| `Action_None` | 112 | 315 | 204 | inferred_complete_timeline |
| `Action_None` | 318 | 319 | 2 | inferred_complete_timeline |
| `Action_None` | 321 | 389 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 10–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 121 | 112 | inferred_complete_timeline |
| `Action_SplitBlock` | 122 | 194 | 73 | inferred_complete_timeline |
| `Action_SplitBlock` | 196 | 210 | 15 | inferred_complete_timeline |
| `Action_None` | 211 | 389 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 10–389
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 114 | 105 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 149 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 210 | 56 | inferred_complete_timeline |
| `Action_None` | 211 | 389 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 10–150
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 114 | 105 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 150 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 10–389
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 111 | 102 | inferred_complete_timeline |
| `Action_BallSnap` | 112 | 127 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 131 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 179 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 210 | 28 | inferred_complete_timeline |
| `Action_None` | 211 | 389 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 10–389
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 114 | 105 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 204 | 90 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 389 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 10–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 114 | 105 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 210 | 96 | inferred_complete_timeline |
| `Action_None` | 211 | 389 | 179 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 10–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 111 | 102 | inferred_complete_timeline |
| `Action_None` | 112 | 389 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 10–216
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 111 | 102 | inferred_complete_timeline |
| `Action_None` | 112 | 167 | 56 | inferred_complete_timeline |
| `Action_None` | 215 | 216 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 10–161
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 111 | 102 | inferred_complete_timeline |
| `Action_None` | 112 | 161 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 10–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 111 | 102 | inferred_complete_timeline |
| `Action_None` | 112 | 389 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 10–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 111 | 102 | inferred_complete_timeline |
| `Action_None` | 112 | 165 | 54 | inferred_complete_timeline |
| `Action_None` | 170 | 389 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 10–389
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 111 | 102 | inferred_complete_timeline |
| `Action_None` | 112 | 232 | 121 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_None` | 246 | 389 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 10–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 111 | 102 | inferred_complete_timeline |
| `Action_None` | 112 | 389 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 10–220
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 111 | 102 | inferred_complete_timeline |
| `Action_None` | 112 | 220 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 10–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 111 | 102 | inferred_complete_timeline |
| `Action_None` | 112 | 389 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 10–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 111 | 102 | inferred_complete_timeline |
| `Action_None` | 112 | 389 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 10–389
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 111 | 102 | inferred_complete_timeline |
| `Action_None` | 112 | 368 | 257 | inferred_complete_timeline |
| `Action_None` | 377 | 389 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 134–389 | 234 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 156–316 | 145 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 174–389 | 216 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 175–176 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 190–196 | 6 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 196–389 | 179 | 4 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 215–218 | 4 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 231–389 | 154 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 268–358 | 47 | 6 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 327–328 | 2 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 331–389 | 56 | 3 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 343–350 | 8 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 348–378 | 13 | 4 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 375–378 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (LT) duration 96 frames exceeds threshold 90 frames [start=115, end=210].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (C) duration 96 frames exceeds threshold 90 frames [start=115, end=210].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [112–127], lower_priority='Action_ZoneBlock' annotated_start=115, effective_Action_ZoneBlock_start=128.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (RG) duration 96 frames exceeds threshold 90 frames [start=115, end=210].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 96 frames exceeds threshold 90 frames [start=115, end=210].
- ⚠️ Action 'Action_None' range [112-290] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-389] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-315] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-372] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-376] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-161] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-368] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-389] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [122-194] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-389] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-165] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-149] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [140-372] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-179] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-389] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-220] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-232] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-204] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-389] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-296] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-316] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-389] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-219] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-389] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-260] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-366] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-275] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-292] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-311] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-317] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-358] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-334] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-345] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-350] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-352] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-361] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '35' has 1 frames without a visible bounding box.
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

</details>
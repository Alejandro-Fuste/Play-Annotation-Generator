# Play-Annotation-Generator Annotation Review — JetSweep_106

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_106`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 65
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `5` | `4` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_LeadBlock` | TE2 | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Toss` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `20` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 57 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `5` | `4` | 58 | START | 58 | 128 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 87 | START | 87 | 98 |
| ✅ EXACT | `Action_LeadBlock` | TE2 | `3` | `2` | 91 | START | 91 | 178 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `12` | `11` | 91 | START | 91 | 178 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `13` | 91 | START | 91 | 178 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `19` | `18` | 91 | START | 91 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 91 | START | 91 | 178 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `22` | `21` | 91 | START | 116 | 178 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 103 | END | 87 | 103 |
| ✅ EXACT | `Action_Toss` | QB | `16` | `15` | 115 | START | 115 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `5` | `4` | 129 | START | 129 | 250 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 178 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_SnapReceive` | 87 | 103 | 17 | inferred_complete_timeline |
| `Action_None` | 104 | 114 | 11 | inferred_complete_timeline |
| `Action_Toss` | 115 | 128 | 14 | inferred_complete_timeline |
| `Action_None` | 129 | 246 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 299 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–280
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_JetMotion` | 58 | 128 | 71 | inferred_complete_timeline |
| `Action_BallCarry` | 129 | 250 | 122 | inferred_complete_timeline |
| `Action_BallCarry` | 254 | 259 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 263 | 280 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 299 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_LeadBlock` | 91 | 178 | 88 | inferred_complete_timeline |
| `Action_None` | 179 | 204 | 26 | inferred_complete_timeline |
| `Action_None` | 210 | 243 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 127 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 178 | 88 | inferred_complete_timeline |
| `Action_None` | 179 | 239 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 178 | 88 | inferred_complete_timeline |
| `Action_None` | 179 | 265 | 87 | inferred_complete_timeline |
| `Action_None` | 269 | 272 | 4 | inferred_complete_timeline |
| `Action_None` | 274 | 299 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_BallSnap` | 87 | 98 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 178 | 63 | inferred_complete_timeline |
| `Action_None` | 179 | 223 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 178 | 88 | inferred_complete_timeline |
| `Action_None` | 179 | 233 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 178 | 88 | inferred_complete_timeline |
| `Action_None` | 179 | 270 | 92 | inferred_complete_timeline |
| `Action_None` | 272 | 294 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 165 | 79 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 109 | 23 | inferred_complete_timeline |
| `Action_None` | 112 | 114 | 3 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_None` | 123 | 130 | 8 | inferred_complete_timeline |
| `Action_None` | 136 | 201 | 66 | inferred_complete_timeline |
| `Action_None` | 206 | 246 | 41 | inferred_complete_timeline |
| `Action_None` | 250 | 299 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 107 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 145 | 59 | inferred_complete_timeline |
| `Action_None` | 148 | 299 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 181 | 95 | inferred_complete_timeline |
| `Action_None` | 185 | 272 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 244 | 158 | inferred_complete_timeline |
| `Action_None` | 246 | 299 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 235 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 299 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 299 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 280 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 223 | 137 | inferred_complete_timeline |
| `Action_None` | 227 | 271 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 108–109 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 127–299 | 173 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 136–288 | 151 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 163–164 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 170–249 | 80 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 178–215 | 17 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 255–271 | 17 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 279–299 | 19 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `22` (C): Annotated start 91 != Inferred start 116
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [87–103], lower_priority='Action_ZoneBlock' annotated_start=91, effective_Action_ZoneBlock_start=104.
- ⚠️ Action 'Action_None' range [179-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-243] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-223] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-271] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [129-250] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [254-259] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [263-280] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-235] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-145] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-181] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-272] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-107] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-233] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-244] for track '12' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-246] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-280] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-246] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-270] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-294] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-127] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-265] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [87-98] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-223] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-246] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-288] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-249] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-207] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-271] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-284] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-293] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '29' has 2 frames without a visible bounding box.
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
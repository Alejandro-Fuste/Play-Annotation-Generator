# Play-Annotation-Generator Annotation Review — JetSweep_41

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_41`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 135
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `3` | `2` |
| ✅ EXACT | `Action_LeadBlock` | TE2 | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Toss` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_SealBlock` | LT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `12` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `7` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 41 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `19` | `18` | 31 | START | 31 | 68 |
| ✅ EXACT | `Action_BallSnap` | C | `3` | `2` | 40 | START | 40 | 54 |
| ✅ EXACT | `Action_LeadBlock` | TE2 | `12` | `11` | 42 | START | 42 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `11` | `10` | 42 | START | 42 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `1` | 42 | START | 42 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `3` | `2` | 42 | START | 55 | 64 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 42 | START | 42 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `8` | `7` | 42 | START | 42 | 57 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 54 | END | 40 | 54 |
| ✅ EXACT | `Action_Toss` | QB | `4` | `3` | 60 | START | 60 | 68 |
| ✅ EXACT | `Action_SealBlock` | LT | `5` | `4` | 68 | START | 68 | 266 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `19` | `18` | 69 | START | 69 | 259 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 108 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 40 | 54 | 15 | inferred_complete_timeline |
| `Action_None` | 55 | 59 | 5 | inferred_complete_timeline |
| `Action_Toss` | 60 | 68 | 9 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 72 | 170 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 65 | 26 | inferred_complete_timeline |
| `Action_None` | 67 | 152 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 64 | 25 | inferred_complete_timeline |
| `Action_None` | 142 | 159 | 18 | inferred_complete_timeline |
| `Action_None` | 162 | 164 | 3 | inferred_complete_timeline |
| `Action_None` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 197 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_LeadBlock` | 42 | 108 | 67 | inferred_complete_timeline |
| `Action_None` | 109 | 123 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 67 | 26 | inferred_complete_timeline |
| `Action_SealBlock` | 68 | 266 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 50 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 71 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 108 | 27 | inferred_complete_timeline |
| `Action_None` | 109 | 170 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_BallSnap` | 40 | 54 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 64 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 75 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 108 | 29 | inferred_complete_timeline |
| `Action_None` | 109 | 198 | 90 | inferred_complete_timeline |
| `Action_None` | 200 | 202 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 57 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 108 | 47 | inferred_complete_timeline |
| `Action_None` | 109 | 148 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 79 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 108 | 27 | inferred_complete_timeline |
| `Action_None` | 109 | 156 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 87 | 48 | inferred_complete_timeline |
| `Action_None` | 91 | 116 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 45 | 6 | inferred_complete_timeline |
| `Action_None` | 49 | 90 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 69 | 30 | inferred_complete_timeline |
| `Action_None` | 82 | 112 | 31 | inferred_complete_timeline |
| `Action_None` | 116 | 136 | 21 | inferred_complete_timeline |
| `Action_None` | 139 | 186 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 39 | 23 | inferred_complete_timeline |
| `Action_None` | 40 | 112 | 73 | inferred_complete_timeline |
| `Action_None` | 114 | 198 | 85 | inferred_complete_timeline |
| `Action_None` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_None` | 210 | 265 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 55 | 16 | inferred_complete_timeline |
| `Action_None` | 61 | 73 | 13 | inferred_complete_timeline |
| `Action_None` | 84 | 114 | 31 | inferred_complete_timeline |
| `Action_None` | 116 | 193 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 79 | 40 | inferred_complete_timeline |
| `Action_None` | 85 | 87 | 3 | inferred_complete_timeline |
| `Action_None` | 89 | 95 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 198 | 159 | inferred_complete_timeline |
| `Action_None` | 203 | 227 | 25 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 232 | 239 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–87 | 85 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 3–95 | 61 | 8 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 31–299 | 236 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 59–163 | 105 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 94–95 | 2 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 94–174 | 22 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 96–166 | 71 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 103–148 | 43 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 105–136 | 32 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 105–161 | 57 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 113–136 | 24 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 130–138 | 9 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 135–197 | 63 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 139–198 | 60 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 140–245 | 88 | 4 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 162–168 | 7 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 199–253 | 52 | 2 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 199–200 | 2 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 224–254 | 26 | 2 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 260–295 | 36 | 1 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 271–275 | 4 | 2 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 275–293 | 19 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [40–54], lower_priority='Action_ZoneBlock' annotated_start=42, effective_Action_ZoneBlock_start=55.
- ⚠️ Action 'Action_None' range [40-198] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-227] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-239] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-79] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-156] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-64] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-75] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-198] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-170] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-67] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [68-266] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-65] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-152] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-64] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-159] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-197] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-57] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-148] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-87] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-116] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-79] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-50] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-71] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-170] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-69] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-186] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-73] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-193] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-73] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-79] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-112] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-198] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-265] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-10] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-25] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-34] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-56] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-75] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [31-68] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [69-259] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-163] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-174] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-166] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-138] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-161] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-136] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-138] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-198] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-155] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-197] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-245] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-168] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-253] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-254] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-295] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-293] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
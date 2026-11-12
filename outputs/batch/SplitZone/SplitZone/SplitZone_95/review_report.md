# Play-Annotation-Generator Annotation Review — SplitZone_95

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_95`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 58
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `15` | `15` |
| ✅ EXACT | `Action_BlockSecondLevel` | DT1 | defense | `9` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 1 | START | 2 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 1 | START | 2 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 1 | START | 2 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 1 | START | 2 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 1 | START | 2 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 1 | START | 2 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 1 | START | 2 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 1 | START | 2 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 1 | START | 11 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 1 | START | 2 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `6` | `Group` | 1 | START | 2 | 56 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 49 | START | 49 | 62 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `16` | `16` | 52 | START | 52 | 112 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `19` | `19` | 52 | START | 112 | 141 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `20` | 52 | START | 52 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 52 | START | 54 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `3` | 52 | START | 52 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | `6` | `6` | 57 | START | 57 | 129 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 65 | END | 49 | 65 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `18` | 71 | START | 71 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `15` | `15` | 78 | START | 78 | 114 |
| ✅ EXACT | `Action_BlockSecondLevel` | DT1 | `9` | `9` | 86 | START | 86 | 141 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 141 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 49 | 65 | 17 | inferred_complete_timeline |
| `Action_None` | 66 | 70 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 71 | 77 | 7 | inferred_complete_timeline |
| `Action_None` | 78 | 299 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 77 | 76 | inferred_complete_timeline |
| `Action_BallCarry` | 78 | 114 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 124 | 253 | 130 | inferred_complete_timeline |
| `Action_BallCarry` | 255 | 257 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 259 | 299 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 2–248
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 56 | 55 | inferred_complete_timeline |
| `Action_SplitBlock` | 57 | 129 | 73 | inferred_complete_timeline |
| `Action_SplitBlock` | 134 | 141 | 8 | inferred_complete_timeline |
| `Action_None` | 142 | 248 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_None` | 49 | 299 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_None` | 49 | 299 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_None` | 49 | 299 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 2–134
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 51 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 111 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 126 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 134 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 11–299
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 30 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 68 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 141 | 37 | inferred_complete_timeline |
| `Action_None` | 142 | 299 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 2–212
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_BallSnap` | 49 | 62 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 141 | 30 | inferred_complete_timeline |
| `Action_None` | 142 | 212 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 2–112
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 51 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 112 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 2–77
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 51 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 77 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 2–297
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_None` | 49 | 111 | 63 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 161 | 15 | inferred_complete_timeline |
| `Action_None` | 163 | 292 | 130 | inferred_complete_timeline |
| `Action_None` | 294 | 297 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_None` | 49 | 299 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 85 | 84 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 86 | 141 | 56 | inferred_complete_timeline |
| `Action_None` | 142 | 151 | 10 | inferred_complete_timeline |
| `Action_None` | 156 | 299 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 2–113
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_None` | 49 | 113 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_None` | 49 | 129 | 81 | inferred_complete_timeline |
| `Action_None` | 132 | 250 | 119 | inferred_complete_timeline |
| `Action_None` | 254 | 299 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_None` | 49 | 122 | 74 | inferred_complete_timeline |
| `Action_None` | 124 | 299 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_None` | 49 | 299 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_None` | 49 | 299 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_None` | 49 | 299 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_None` | 49 | 299 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_None` | 49 | 299 | 251 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 79–92 | 14 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 90–299 | 206 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 128–299 | 172 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 130–299 | 170 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 135–299 | 165 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 214–299 | 85 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 225–279 | 22 | 5 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 245–247 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `19` (C): Annotated start 52 != Inferred start 112
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [49–65], lower_priority='Action_ZoneBlock' annotated_start=52, effective_Action_ZoneBlock_start=66.
- ⚠️ Action 'Action_ZoneBlock' range [52-111] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-134] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [57-129] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-248] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-111] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-161] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-292] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-151] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-113] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-250] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [78-114] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [124-253] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [255-257] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-122] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [49-62] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 142, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [142-212] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-30] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-93] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-92] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-105] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-299] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-255] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '29' has 1 frames without a visible bounding box.
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
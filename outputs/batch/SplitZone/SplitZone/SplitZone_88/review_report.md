# Play-Annotation-Generator Annotation Review — SplitZone_88

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_88`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 133
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 100
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | DT2 | defense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 3 | START | 4 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 3 | START | 11 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 3 | START | 4 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 3 | START | 4 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 3 | START | 4 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 3 | START | 4 | 15 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 88 | START | 88 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 91 | START | 104 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `17` | `17` | 91 | START | 145 | 160 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `5` | 91 | START | 91 | 185 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `8` | 91 | START | 91 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | DT2 | `14` | `14` | 96 | START | 96 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `3` | `3` | 103 | END | 88 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `4` | 123 | START | 123 | 145 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 185 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 4–158
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 87 | 84 | inferred_complete_timeline |
| `Action_SnapReceive` | 88 | 98 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 103 | 103 | 1 | inferred_complete_timeline |
| `Action_None` | 104 | 123 | 20 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 137 | 145 | 9 | inferred_complete_timeline |
| `Action_None` | 149 | 158 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 4–174
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 122 | 119 | inferred_complete_timeline |
| `Action_BallCarry` | 123 | 145 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 170 | 174 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 11–269
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 21 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 40 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 59 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 66 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 79 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 160 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 165 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 185 | 13 | inferred_complete_timeline |
| `Action_None` | 186 | 269 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 4–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 90 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 185 | 95 | inferred_complete_timeline |
| `Action_None` | 186 | 197 | 12 | inferred_complete_timeline |
| `Action_None` | 200 | 226 | 27 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |
| `Action_None` | 242 | 269 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 4–252
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 87 | 84 | inferred_complete_timeline |
| `Action_BallSnap` | 88 | 103 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 138 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 149 | 5 | inferred_complete_timeline |
| `Action_None` | 187 | 240 | 54 | inferred_complete_timeline |
| `Action_None` | 244 | 252 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 4–114
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 15 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 90 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 114 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 4–256
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 87 | 84 | inferred_complete_timeline |
| `Action_None` | 88 | 137 | 50 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 149 | 6 | inferred_complete_timeline |
| `Action_None` | 153 | 158 | 6 | inferred_complete_timeline |
| `Action_None` | 166 | 171 | 6 | inferred_complete_timeline |
| `Action_None` | 174 | 228 | 55 | inferred_complete_timeline |
| `Action_None` | 230 | 247 | 18 | inferred_complete_timeline |
| `Action_None` | 250 | 256 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 4–190
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 87 | 84 | inferred_complete_timeline |
| `Action_None` | 88 | 124 | 37 | inferred_complete_timeline |
| `Action_None` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_None` | 184 | 190 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 4–269
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 32 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 87 | 53 | inferred_complete_timeline |
| `Action_None` | 88 | 109 | 22 | inferred_complete_timeline |
| `Action_None` | 151 | 154 | 4 | inferred_complete_timeline |
| `Action_None` | 178 | 182 | 5 | inferred_complete_timeline |
| `Action_None` | 191 | 199 | 9 | inferred_complete_timeline |
| `Action_None` | 204 | 209 | 6 | inferred_complete_timeline |
| `Action_None` | 211 | 224 | 14 | inferred_complete_timeline |
| `Action_None` | 226 | 234 | 9 | inferred_complete_timeline |
| `Action_None` | 239 | 269 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 7–269
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 12 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 95 | 79 | inferred_complete_timeline |
| `Action_SplitBlock` | 96 | 134 | 39 | inferred_complete_timeline |
| `Action_SplitBlock` | 138 | 160 | 23 | inferred_complete_timeline |
| `Action_SplitBlock` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_SplitBlock` | 174 | 185 | 12 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 269 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 4–266
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 87 | 84 | inferred_complete_timeline |
| `Action_None` | 88 | 266 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 4–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 87 | 84 | inferred_complete_timeline |
| `Action_None` | 88 | 150 | 63 | inferred_complete_timeline |
| `Action_None` | 155 | 269 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 4–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 25 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 87 | 60 | inferred_complete_timeline |
| `Action_None` | 88 | 129 | 42 | inferred_complete_timeline |
| `Action_None` | 132 | 269 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 4–172
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 87 | 84 | inferred_complete_timeline |
| `Action_None` | 88 | 104 | 17 | inferred_complete_timeline |
| `Action_None` | 116 | 120 | 5 | inferred_complete_timeline |
| `Action_None` | 125 | 144 | 20 | inferred_complete_timeline |
| `Action_None` | 149 | 172 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 4–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 87 | 84 | inferred_complete_timeline |
| `Action_None` | 88 | 269 | 182 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 4–29 | 26 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 8–269 | 262 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 9–269 | 130 | 7 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 104–194 | 85 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 115–213 | 95 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 122–269 | 133 | 5 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 134–138 | 5 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 145–159 | 14 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 165–204 | 40 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 202–269 | 64 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 220–269 | 50 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 227–237 | 10 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 232–248 | 9 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 233–253 | 9 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 240–269 | 30 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 269–269 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 94 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 178: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 178: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (LG) duration 95 frames exceeds threshold 90 frames [start=91, end=185].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 95 frames exceeds threshold 90 frames [start=91, end=185].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [88–103], lower_priority='Action_ZoneBlock' annotated_start=91, effective_Action_ZoneBlock_start=104.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (LT) duration 95 frames exceeds threshold 90 frames [start=91, end=185].
- ⚠️ Action 'Action_PreSnap' range [4-87] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-124] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-190] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-137] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-149] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-228] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-247] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-256] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [88-98] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-123] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-145] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [123-145] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [170-174] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-185] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-197] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-226] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-29] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-32] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-199] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-209] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-234] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-15] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-266] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-25] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-144] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-172] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [88-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-138] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [145-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-240] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-252] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-12] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [96-134] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [138-160] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [164-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-69] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-160] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-197] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-215] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-21] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-40] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-59] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [145-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-160] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-194] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-213] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-163] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-179] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-138] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-154] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-204] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-213] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-237] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>
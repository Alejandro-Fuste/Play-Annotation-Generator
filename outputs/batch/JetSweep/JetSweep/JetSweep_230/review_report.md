# Play-Annotation-Generator Annotation Review — JetSweep_230

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_230`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 133
- **Validation Warnings:** 155
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `4` | `3` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | LT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Toss` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `4` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_JetMotion` | WR | `4` | `3` | 7 | START | 7 | 48 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 24 | START | 24 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | LT | `10` | `9` | 25 | START | 25 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `10` | 25 | START | 38 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `10` | 25 | START | 38 | 71 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `12` | `11` | 25 | START | 25 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `13` | 25 | START | 25 | 34 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `1` | 25 | START | 25 | 152 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 37 | END | 24 | 37 |
| ✅ EXACT | `Action_Toss` | QB | `5` | `4` | 45 | START | 45 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `4` | `3` | 49 | START | 49 | 50 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 152 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–232
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 37 | 14 | inferred_complete_timeline |
| `Action_None` | 38 | 44 | 7 | inferred_complete_timeline |
| `Action_Toss` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_None` | 49 | 68 | 20 | inferred_complete_timeline |
| `Action_None` | 70 | 92 | 23 | inferred_complete_timeline |
| `Action_None` | 100 | 106 | 7 | inferred_complete_timeline |
| `Action_None` | 190 | 222 | 33 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 55 | 32 | inferred_complete_timeline |
| `Action_None` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_None` | 68 | 153 | 86 | inferred_complete_timeline |
| `Action_None` | 164 | 194 | 31 | inferred_complete_timeline |
| `Action_None` | 200 | 204 | 5 | inferred_complete_timeline |
| `Action_None` | 207 | 222 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_JetMotion` | 7 | 48 | 42 | inferred_complete_timeline |
| `Action_BallCarry` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 53 | 61 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 65 | 86 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 103 | 108 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 111 | 138 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 37 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_LeadBlock` | 25 | 48 | 24 | inferred_complete_timeline |
| `Action_LeadBlock` | 50 | 55 | 6 | inferred_complete_timeline |
| `Action_LeadBlock` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_LeadBlock` | 65 | 72 | 8 | inferred_complete_timeline |
| `Action_LeadBlock` | 75 | 82 | 8 | inferred_complete_timeline |
| `Action_LeadBlock` | 92 | 120 | 29 | inferred_complete_timeline |
| `Action_LeadBlock` | 123 | 138 | 16 | inferred_complete_timeline |
| `Action_LeadBlock` | 142 | 152 | 11 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 34 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 39 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 55 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 68 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 77 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_BallSnap` | 24 | 37 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 71 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 77 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 111 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 152 | 34 | inferred_complete_timeline |
| `Action_None` | 153 | 239 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 42 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 152 | 128 | inferred_complete_timeline |
| `Action_None` | 153 | 234 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 66 | 43 | inferred_complete_timeline |
| `Action_None` | 68 | 123 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 87 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 7 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 23 | 1 | inferred_complete_timeline |
| `Action_None` | 24 | 29 | 6 | inferred_complete_timeline |
| `Action_None` | 33 | 34 | 2 | inferred_complete_timeline |
| `Action_None` | 36 | 84 | 49 | inferred_complete_timeline |
| `Action_None` | 97 | 113 | 17 | inferred_complete_timeline |
| `Action_None` | 115 | 174 | 60 | inferred_complete_timeline |
| `Action_None` | 179 | 220 | 42 | inferred_complete_timeline |
| `Action_None` | 227 | 232 | 6 | inferred_complete_timeline |
| `Action_None` | 236 | 238 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 109 | 86 | inferred_complete_timeline |
| `Action_None` | 117 | 239 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 155 | 132 | inferred_complete_timeline |
| `Action_None` | 157 | 170 | 14 | inferred_complete_timeline |
| `Action_None` | 174 | 179 | 6 | inferred_complete_timeline |
| `Action_None` | 183 | 186 | 4 | inferred_complete_timeline |
| `Action_None` | 188 | 198 | 11 | inferred_complete_timeline |
| `Action_None` | 202 | 239 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 88 | 65 | inferred_complete_timeline |
| `Action_None` | 90 | 97 | 8 | inferred_complete_timeline |
| `Action_None` | 102 | 239 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 2–198 | 158 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 29–212 | 156 | 7 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 50–81 | 32 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 59–239 | 149 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 81–239 | 145 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 83–207 | 123 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 88–239 | 146 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 90–209 | 115 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 97–116 | 20 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 102–103 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 107–239 | 132 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 112–239 | 128 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 116–118 | 3 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 131–206 | 73 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 136–138 | 3 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 143–237 | 81 | 5 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 144–164 | 21 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 180–239 | 60 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 184–220 | 37 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 187–190 | 4 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 203–239 | 37 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 212–222 | 10 | 2 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 232–234 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `10` (8 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 103 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (RT) duration 128 frames exceeds threshold 90 frames [start=25, end=152].
- ⚠️ Overlapping action conflict at frame 25 for track '9': 'Action_ZoneBlock' vs 'Action_LeadBlock'. Overriding with 'Action_LeadBlock'.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '9' (LT) duration 128 frames exceeds threshold 90 frames [start=25, end=152].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (C) duration 128 frames exceeds threshold 90 frames [start=25, end=152].
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [24–37], lower_priority='Action_ZoneBlock' annotated_start=25, effective_Action_ZoneBlock_start=38.
- ⚠️ Action 'Action_None' range [24-87] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-234] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-155] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-170] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-179] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-198] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [49-50] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [53-61] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [65-86] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [97-98] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [103-108] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [111-138] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-68] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-66] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-123] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-109] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-239] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-55] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-153] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-194] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-204] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-222] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-37] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [25-48] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [50-55] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [61-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [65-72] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [75-82] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [92-120] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [123-138] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-71] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-111] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-42] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-88] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-97] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-34] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [37-39] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-68] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-7] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-29] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-34] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-174] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-220] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-232] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-154] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-34] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-41] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-126] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-192] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-81] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-72] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-154] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-222] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-203] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-176] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-197] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-159] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-197] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-209] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-116] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-124] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-155] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-163] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-234] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-164] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-239] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-222] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
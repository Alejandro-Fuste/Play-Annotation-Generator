# Play-Annotation-Generator Annotation Review — JetSweep_198

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_198`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 57
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 169
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 94
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Toss` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 51 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `18` | `17` | 33 | START | 33 | 72 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 51 | START | 51 | 59 |
| ✅ EXACT | `Action_LeadBlock` | TE | `9` | `8` | 52 | START | 52 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `14` | 52 | START | 60 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `16` | `15` | 52 | START | 52 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `2` | `1` | 52 | START | 52 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `5` | 52 | START | 52 | 96 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `6` | 52 | START | 52 | 100 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 59 | END | 51 | 59 |
| ✅ EXACT | `Action_Toss` | QB | `14` | `13` | 69 | START | 69 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `18` | `17` | 73 | START | 73 | 287 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 101 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_SnapReceive` | 51 | 59 | 9 | inferred_complete_timeline |
| `Action_None` | 60 | 68 | 9 | inferred_complete_timeline |
| `Action_Toss` | 69 | 72 | 4 | inferred_complete_timeline |
| `Action_None` | 73 | 113 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 105 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_LeadBlock` | 52 | 101 | 50 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 73 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 84 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 97 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 101 | 1 | inferred_complete_timeline |
| `Action_None` | 102 | 102 | 1 | inferred_complete_timeline |
| `Action_None` | 107 | 123 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 83 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 101 | 13 | inferred_complete_timeline |
| `Action_None` | 102 | 107 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_BallSnap` | 51 | 59 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 101 | 42 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 100 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 96 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 50 | 11 | inferred_complete_timeline |
| `Action_None` | 51 | 68 | 18 | inferred_complete_timeline |
| `Action_None` | 71 | 118 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 75 | 25 | inferred_complete_timeline |
| `Action_None` | 79 | 82 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 76 | 26 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_None` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 141 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 111 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 161 | 111 | inferred_complete_timeline |
| `Action_None` | 163 | 329 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 98 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 150 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 329 | 279 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 33–329 | 294 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 85–91 | 7 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 114–117 | 4 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 119–329 | 211 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 123–150 | 28 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 126–227 | 98 | 3 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 130–131 | 2 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 172–217 | 38 | 3 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 177–318 | 133 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 179–258 | 11 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 198–202 | 5 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 213–216 | 4 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 219–242 | 24 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 231–235 | 5 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 232–262 | 12 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 236–259 | 24 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 246–247 | 2 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 256–327 | 53 | 5 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 256–264 | 6 | 2 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 257–328 | 50 | 2 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 275–315 | 34 | 3 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 279–329 | 51 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 281–282 | 2 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 288–329 | 42 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 294–329 | 36 | 1 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 297–329 | 32 | 2 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 299–315 | 6 | 2 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 299–329 | 31 | 1 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 304–329 | 26 | 1 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 305–312 | 8 | 1 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 306–321 | 12 | 2 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 307–329 | 23 | 1 | Undefined position; Undefined team |
| `49` | `68` | Position_Unknown | Team_Unknown | 308–321 | 14 | 1 | Undefined position; Undefined team |
| `50` | `69` | Position_Unknown | Team_Unknown | 310–329 | 19 | 2 | Undefined position; Undefined team |
| `51` | `71` | Position_Unknown | Team_Unknown | 314–321 | 7 | 2 | Undefined position; Undefined team |
| `52` | `72` | Position_Unknown | Team_Unknown | 314–317 | 4 | 1 | Undefined position; Undefined team |
| `53` | `73` | Position_Unknown | Team_Unknown | 318–329 | 10 | 2 | Undefined position; Undefined team |
| `54` | `74` | Position_Unknown | Team_Unknown | 318–322 | 5 | 1 | Undefined position; Undefined team |
| `55` | `75` | Position_Unknown | Team_Unknown | 319–324 | 6 | 1 | Undefined position; Undefined team |
| `56` | `76` | Position_Unknown | Team_Unknown | 323–329 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 40 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 40 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 80 |
| Missing visible bounding boxes during action | 87 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [51–59], lower_priority='Action_ZoneBlock' annotated_start=52, effective_Action_ZoneBlock_start=60.
- ⚠️ Action 'Action_None' range [51-111] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-83] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-161] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-105] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-96] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [52-101] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-141] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-76] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-118] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-113] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-101] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-73] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-84] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-97] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 102, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [102-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-75] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [73-287] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-91] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-139] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-227] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-206] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-190] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-318] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-242] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-239] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-259] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-321] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-327] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-259] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-328] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-315] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-329] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-329] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-301] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-312] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-309] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-321] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-321] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-325] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-321] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-317] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-325] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-322] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-324] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '56' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.

</details>
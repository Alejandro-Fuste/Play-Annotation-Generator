# Play-Annotation-Generator Annotation Review — SplitZone_155

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_155`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 45
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `17` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `8` |
| ✅ EXACT | `Action_BlockSecondLevel` | DT2 | defense | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 19 | START | 20 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 19 | START | 20 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 19 | START | 20 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 19 | START | 20 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `16` | `Group` | 19 | START | 20 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 19 | START | 20 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 19 | START | 20 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 19 | START | 20 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 19 | START | 20 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 19 | START | 20 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 19 | START | 20 | 118 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 89 | START | 89 | 93 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `12` | `12` | 92 | START | 92 | 161 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `14` | 92 | START | 94 | 101 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `15` | 92 | START | 92 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 92 | START | 92 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 92 | START | 92 | 156 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 93 | END | 89 | 93 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `17` | `17` | 93 | START | 93 | 161 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `18` | 110 | START | 110 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `8` | 119 | START | 119 | 203 |
| ✅ EXACT | `Action_BlockSecondLevel` | DT2 | `10` | `10` | 126 | START | 126 | 161 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 161 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 20–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 88 | 69 | inferred_complete_timeline |
| `Action_SnapReceive` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_None` | 94 | 109 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 110 | 118 | 9 | inferred_complete_timeline |
| `Action_None` | 119 | 239 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 20–237
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 118 | 99 | inferred_complete_timeline |
| `Action_BallCarry` | 119 | 203 | 85 | inferred_complete_timeline |
| `Action_BallCarry` | 212 | 237 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 20–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 88 | 69 | inferred_complete_timeline |
| `Action_None` | 89 | 239 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 20–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 88 | 69 | inferred_complete_timeline |
| `Action_None` | 89 | 239 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 20–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 88 | 69 | inferred_complete_timeline |
| `Action_None` | 89 | 239 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 20–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 92 | 73 | inferred_complete_timeline |
| `Action_SplitBlock` | 93 | 161 | 69 | inferred_complete_timeline |
| `Action_None` | 162 | 239 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 20–110
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 91 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 110 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 20–239
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 91 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 156 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 161 | 1 | inferred_complete_timeline |
| `Action_None` | 162 | 239 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 20–101
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 88 | 69 | inferred_complete_timeline |
| `Action_BallSnap` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 101 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 20–239
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 91 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 109 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 161 | 42 | inferred_complete_timeline |
| `Action_None` | 162 | 239 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 20–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 91 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 161 | 70 | inferred_complete_timeline |
| `Action_None` | 162 | 239 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 20–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 88 | 69 | inferred_complete_timeline |
| `Action_None` | 89 | 125 | 37 | inferred_complete_timeline |
| `Action_None` | 128 | 239 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 20–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 88 | 69 | inferred_complete_timeline |
| `Action_None` | 89 | 239 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 20–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 88 | 69 | inferred_complete_timeline |
| `Action_None` | 89 | 119 | 31 | inferred_complete_timeline |
| `Action_None` | 121 | 239 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 20–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 125 | 106 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 126 | 161 | 36 | inferred_complete_timeline |
| `Action_None` | 162 | 239 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 20–117
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 88 | 69 | inferred_complete_timeline |
| `Action_None` | 89 | 104 | 16 | inferred_complete_timeline |
| `Action_None` | 113 | 117 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 20–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 88 | 69 | inferred_complete_timeline |
| `Action_None` | 89 | 239 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 20–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 88 | 69 | inferred_complete_timeline |
| `Action_None` | 89 | 239 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 20–239
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 88 | 69 | inferred_complete_timeline |
| `Action_None` | 91 | 223 | 133 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 20–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 88 | 69 | inferred_complete_timeline |
| `Action_None` | 89 | 239 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 20–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 88 | 69 | inferred_complete_timeline |
| `Action_None` | 89 | 239 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 20–143
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 88 | 69 | inferred_complete_timeline |
| `Action_None` | 89 | 143 | 55 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 57–138 | 5 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 111–239 | 122 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 112–239 | 128 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 117–238 | 122 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 147–151 | 5 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 154–239 | 86 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 171–181 | 11 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 192–235 | 38 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 92 != Inferred start 94
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 27 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [89–93], lower_priority='Action_ZoneBlock' annotated_start=92, effective_Action_ZoneBlock_start=94.
- ⚠️ Action 'Action_None' range [89-104] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-117] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-125] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-239] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-119] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-88] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-223] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [119-203] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [212-237] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-143] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-110] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-109] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-161] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-156] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-58] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-128] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-239] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-238] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-181] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-235] for track '29' has 2 frames without a visible bounding box.
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
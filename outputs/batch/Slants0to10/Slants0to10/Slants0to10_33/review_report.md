# Play-Annotation-Generator Annotation Review — Slants0to10_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_33`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunSlantRoute` | WR3 | offense | `9` | `9` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `14` | `14` | 2 | START | 2 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 2 | START | 2 | 11 |
| ✅ EXACT | `Action_PassBlock` | C | `19` | `19` | 2 | START | 2 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `20` | `20` | 2 | START | 2 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 2 | START | 2 | 11 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 2 | END | 2 | 2 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunSlantRoute` | WR3 | `9` | `9` | 20 | START | 20 | 21 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 47 | START | 47 | 57 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `9` | `9` | 91 | START | 91 | 94 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 2 | 1 | inferred_complete_timeline |
| `Action_None` | 3 | 46 | 44 | inferred_complete_timeline |
| `Action_ThrowPass` | 47 | 57 | 11 | inferred_complete_timeline |
| `Action_None` | 58 | 127 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 61 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 93 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 75 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 91 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 106 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 239 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 24 | 28 | 5 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 31 | 66 | 36 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_None` | 70 | 90 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 91 | 94 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 118 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 11 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 35 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 93 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–27
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 27 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 11 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 36 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 48 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 66 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 44 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 66 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 105 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 183 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 198 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 128 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 115 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 127 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 68 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 88 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 97 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 104 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 239 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 92 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 170 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 191 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 205 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 214 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 25–36 | 12 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 53–120 | 41 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 62–67 | 6 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 66–239 | 173 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 95–100 | 6 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 102–144 | 43 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 106–135 | 30 | 1 | Undefined position; Undefined team |
| `29` | `45` | Position_Unknown | Team_Unknown | 116–130 | 15 | 1 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 117–147 | 31 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 122–141 | 20 | 1 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 144–145 | 2 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 148–210 | 61 | 2 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 167–239 | 73 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 182–239 | 58 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 184–239 | 56 | 1 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 189–239 | 49 | 3 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 204–239 | 32 | 3 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 222–226 | 5 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 234–239 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunSlantRoute` and target `9` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 77 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-75] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-91] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-106] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-92] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-170] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-205] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-214] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-115] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-127] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-68] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-88] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-67] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-128] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-61] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-93] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunSlantRoute' range [20-21] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunSlantRoute' range [24-28] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunSlantRoute' range [31-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [91-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-183] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-198] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-115] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-66] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-104] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-11] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-35] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-40] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-93] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-27] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-48] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-52] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-118] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-11] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-36] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-55] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-66] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-36] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-55] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-67] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-120] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-67] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-115] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-100] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-144] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-135] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-130] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-147] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-141] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-202] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-194] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-206] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-210] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-217] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-226] for track '39' has 2 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>
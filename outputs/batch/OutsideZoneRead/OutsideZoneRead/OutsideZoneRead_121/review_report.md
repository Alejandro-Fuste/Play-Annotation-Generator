# Play-Annotation-Generator Annotation Review — OutsideZoneRead_121

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_121`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 121
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_Keep` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `21` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 34 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 35 | START | 35 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `12` | `11` | 38 | START | 38 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `16` | 38 | START | 38 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `17` | 38 | START | 49 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `19` | 38 | START | 38 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `22` | `21` | 38 | START | 38 | 61 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 48 | END | 35 | 48 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `19` | `18` | 52 | START | 52 | 55 |
| ✅ EXACT | `Action_Keep` | QB | `19` | `18` | 56 | START | 56 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `19` | `18` | 77 | START | 77 | 174 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 99 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_SnapReceive` | 35 | 48 | 14 | inferred_complete_timeline |
| `Action_None` | 49 | 51 | 3 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 52 | 55 | 4 | inferred_complete_timeline |
| `Action_Keep` | 56 | 76 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 77 | 174 | 98 | inferred_complete_timeline |
| `Action_BallCarry` | 176 | 210 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 60 | 26 | inferred_complete_timeline |
| `Action_None` | 66 | 138 | 73 | inferred_complete_timeline |
| `Action_None` | 143 | 172 | 30 | inferred_complete_timeline |
| `Action_None` | 174 | 210 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 146 | 112 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 164 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 120 | 86 | inferred_complete_timeline |
| `Action_None` | 125 | 130 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 210 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 61 | 27 | inferred_complete_timeline |
| `Action_None` | 65 | 80 | 16 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 131 | 28 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 202 | 4 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 74 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 87 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 61 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 74 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_BallSnap` | 35 | 48 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 74 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 93 | 3 | inferred_complete_timeline |
| `Action_None` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_None` | 123 | 210 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 55 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 75 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 84 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 61 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 74 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 87 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 76 | 42 | inferred_complete_timeline |
| `Action_None` | 90 | 141 | 52 | inferred_complete_timeline |
| `Action_None` | 148 | 173 | 26 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 59 | 25 | inferred_complete_timeline |
| `Action_None` | 70 | 71 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 66 | 32 | inferred_complete_timeline |
| `Action_None` | 69 | 74 | 6 | inferred_complete_timeline |
| `Action_None` | 128 | 132 | 5 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_None` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_None` | 167 | 176 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 61 | 27 | inferred_complete_timeline |
| `Action_None` | 63 | 66 | 4 | inferred_complete_timeline |
| `Action_None` | 69 | 74 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 77 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 86 | 52 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 109 | 75 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 202 | 34 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 141 | 107 | inferred_complete_timeline |
| `Action_None` | 143 | 148 | 6 | inferred_complete_timeline |
| `Action_None` | 150 | 160 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 142 | 108 | inferred_complete_timeline |
| `Action_None` | 155 | 157 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 210 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 180 | 146 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 112–210 | 98 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 116–131 | 12 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 120–210 | 90 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 124–210 | 86 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 126–210 | 85 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 126–141 | 14 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 129–139 | 5 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 138–210 | 73 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 143–174 | 5 | 2 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 158–173 | 12 | 3 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 168–210 | 43 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 174–210 | 37 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 189–210 | 22 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 194–210 | 17 | 1 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 198–201 | 4 | 1 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 198–210 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 96 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [35–48], lower_priority='Action_ZoneBlock' annotated_start=38, effective_Action_ZoneBlock_start=49.
- ⚠️ Action 'Action_None' range [35-76] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-141] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-173] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-59] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-130] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-146] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-86] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-109] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-202] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-142] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-77] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-61] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-74] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-66] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-176] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-87] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-160] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-138] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-172] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-210] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-61] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [35-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-74] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-87] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [56-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [77-174] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [176-210] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-55] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-61] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-74] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-118] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-201] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-131] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-131] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-141] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-164] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '37' has 1 frames without a visible bounding box.
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
# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_297`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_297/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 107 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [3–18], lower_priority='Action_ZoneBlock' annotated_start=6, effective_Action_ZoneBlock_start=19.
> - Action 'Action_None' range [3-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-101] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-87] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-54] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-107] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-120] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-92] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-40] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-96] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-176] for track '6' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [187-193] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-24] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-55] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-124] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-134] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [52-95] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [103-107] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [110-114] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [118-123] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [128-139] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [141-151] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [162-165] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [173-174] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-202] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [205-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-99] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-210] for track '10' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [3-161] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-56] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-41] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-210] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [19-28] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-31] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-67] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [75-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-54] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-12] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-28] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-73] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-210] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [83-85] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-130] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-184] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-196] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-197] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '33' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
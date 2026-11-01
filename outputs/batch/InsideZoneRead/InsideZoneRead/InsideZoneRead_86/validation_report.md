# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_86`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_86/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 174: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [53–58], lower_priority='Action_ZoneBlock' annotated_start=56, effective_Action_ZoneBlock_start=59.
> - Action 'Action_None' range [53-129] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [131-169] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-71] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-128] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-98] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-135] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-108] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-154] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-143] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-120] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [105-115] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-143] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-208] for track '9' has 5 frames without a visible bounding box.
> - Action 'Action_Handoff' range [83-87] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-76] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-80] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-121] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-180] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [97-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [104-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [130-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [138-156] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [158-159] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [161-172] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [53-58] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-58] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-193] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-100] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [102-121] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-139] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-146] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-153] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-145] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-165] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-165] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-207] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-187] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-192] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-168] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '29' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
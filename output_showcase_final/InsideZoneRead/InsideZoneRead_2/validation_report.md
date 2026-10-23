# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_2`
- **Input XML**: `output_showcase_final/InsideZoneRead/InsideZoneRead_2/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 6: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [55–68], lower_priority='Action_ZoneBlock' annotated_start=57, effective_Action_ZoneBlock_start=69.
> - Action 'Action_None' range [55-164] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-78] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-87] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-229] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [88-98] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [82-86] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [57-65] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-140] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-102] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-125] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-141] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-233] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [57-83] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-88] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-84] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-111] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-122] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [57-75] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-171] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-211] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-125] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-96] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-119] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-138] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-157] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-165] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-179] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-185] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-216] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-107] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-140] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-153] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-169] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-194] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-219] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-179] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-188] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-187] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-214] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-213] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-238] for track '23' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
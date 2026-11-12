# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_124`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_124/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 108 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [44–56], lower_priority='Action_ZoneBlock' annotated_start=47, effective_Action_ZoneBlock_start=57.
> - Action 'Action_None' range [44-122] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-196] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-130] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-181] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-214] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-71] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-115] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-231] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-115] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-219] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-121] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-79] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-193] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [71-77] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [79-219] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [57-71] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-122] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [46-74] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-212] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-93] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-106] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-140] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-225] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-269] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-58] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-76] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-102] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-105] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [107-108] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-97] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-74] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-108] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-93] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-137] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-155] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-230] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-152] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [184-216] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-150] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-169] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-208] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-219] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-208] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-246] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-269] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-223] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-188] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-209] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
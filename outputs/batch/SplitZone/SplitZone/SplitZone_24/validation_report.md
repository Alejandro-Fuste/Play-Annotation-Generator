# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_24`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_24/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [60–76], lower_priority='Action_ZoneBlock' annotated_start=63, effective_Action_ZoneBlock_start=77.
> - Action 'Action_BallCarry' for track '0' starts at frame 97, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [97-97] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-81] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-134] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-174] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-190] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-103] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-229] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [66-92] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-94] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-170] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-219] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-72] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-168] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-28] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-222] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-154] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-89] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-168] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-131] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-192] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-118] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-188] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-178] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-25] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-64] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-132] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-24] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-111] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-142] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-219] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-108] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-114] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-118] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-169] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-202] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-214] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-212] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-231] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '31' has 1 frames without a visible bounding box.
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
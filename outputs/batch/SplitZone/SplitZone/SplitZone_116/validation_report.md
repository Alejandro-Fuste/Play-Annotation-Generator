# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_116`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_116/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (RT) duration 96 frames exceeds threshold 90 frames [start=31, end=126].
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (C) duration 96 frames exceeds threshold 90 frames [start=31, end=126].
> - Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [28–38], lower_priority='Action_ZoneBlock' annotated_start=31, effective_Action_ZoneBlock_start=39.
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (RG) duration 96 frames exceeds threshold 90 frames [start=31, end=126].
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (LT) duration 96 frames exceeds threshold 90 frames [start=31, end=126].
> - Action 'Action_None' range [28-184] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-196] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-239] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-43] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-55] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-88] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-166] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-59] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-98] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-208] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-33] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-85] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-103] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [28-33] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-224] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-239] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [32-56] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [59-70] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-212] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-9] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-30] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-48] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-115] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-126] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-29] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-46] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-15] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [56-100] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-186] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-96] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-239] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-239] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [89-94] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-197] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-146] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-169] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-232] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-193] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-208] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-234] for track '31' has 2 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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
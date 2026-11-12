# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_13`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_13/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [82–99], lower_priority='Action_ZoneBlock' annotated_start=85, effective_Action_ZoneBlock_start=100.
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (LG) duration 97 frames exceeds threshold 90 frames [start=85, end=181].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (LT) duration 97 frames exceeds threshold 90 frames [start=85, end=181].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 97 frames exceeds threshold 90 frames [start=85, end=181].
> - Action 'Action_None' range [82-125] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-109] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-267] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-128] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-220] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-262] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-111] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-123] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-171] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-182] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-242] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-170] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-178] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [122-137] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [124-241] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-242] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-259] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-117] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-148] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [150-206] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-261] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-115] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-149] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-107] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-117] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-262] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-241] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-192] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-158] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-168] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-269] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-219] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-222] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-241] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-228] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-246] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-259] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-264] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-261] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-269] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-255] for track '35' has 1 frames without a visible bounding box.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_315`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_315/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '19' has invalid range: start=80, end=32. Clamping end to start.
> - Action 'Action_None' range [71-155] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-419] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-261] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-128] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-160] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-124] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-338] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-91] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-269] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-300] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-308] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-317] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-191] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-389] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-396] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-419] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-111] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-300] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [302-317] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-103] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-419] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-185] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-396] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-409] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-418] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [117-396] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [399-404] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-222] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-17] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-32] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-219] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-311] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-419] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-360] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-391] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-272] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-419] for track '29' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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
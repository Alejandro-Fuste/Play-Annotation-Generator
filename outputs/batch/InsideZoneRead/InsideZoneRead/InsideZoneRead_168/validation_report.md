# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_168`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_168/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 97 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 102 frames exceeds threshold 90 frames [start=55, end=156].
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (C) duration 102 frames exceeds threshold 90 frames [start=55, end=156].
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (RG) duration 102 frames exceeds threshold 90 frames [start=55, end=156].
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (LG) duration 102 frames exceeds threshold 90 frames [start=55, end=156].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (LT) duration 102 frames exceeds threshold 90 frames [start=55, end=156].
> - Action 'Action_BallCarry' range [92-193] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [196-213] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [215-295] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-364] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-419] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-351] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-381] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [52-419] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-360] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-184] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-201] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-282] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-356] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-186] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-419] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-187] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-194] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-173] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-222] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-243] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [246-253] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-287] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-287] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [298-399] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-281] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-182] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-236] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-281] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [157-374] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-371] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-169] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-228] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-247] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-333] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-82] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-128] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-160] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-255] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-266] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-275] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-243] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-257] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-265] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-299] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-378] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-381] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-413] for track '35' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_168'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
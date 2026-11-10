# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_3`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-286] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-235] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-213] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-222] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-241] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-252] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-261] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-217] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-241] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-250] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-283] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-231] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-274] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-283] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [230-240] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [241-245] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [252-269] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-244] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-213] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-220] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-207] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-213] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-207] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-185] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-192] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-219] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-282] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-296] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-238] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-281] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-299] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-295] for track '32' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
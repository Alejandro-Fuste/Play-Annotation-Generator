# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_12`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_12/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 27 |
| Ball Tracks | 1 |
| CSV events parsed | 10 |
| Action Segments inferred | 47 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 14, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '210,?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-170] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-212] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-173] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-226] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-239] for track '5' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-236] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [151-172] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [176-178] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [181-188] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [223-238] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-141] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-152] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-151] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-187] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-198] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-170] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-211] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-201] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-183] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-200] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-190] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-238] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '27' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
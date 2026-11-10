# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_154`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_154/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [62-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-151] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-70] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-138] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-137] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-122] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-148] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-156] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-134] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [62-133] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-114] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-141] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-101] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-104] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-140] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-76] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-155] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-76] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-93] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-127] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [133-193] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-26] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-43] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [62-143] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-189] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-200] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-195] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-186] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-198] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-206] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
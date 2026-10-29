# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_217`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_217/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 33 |
| Ball Tracks | 1 |
| CSV events parsed | 14 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 436: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Track ID '6' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-3] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-202] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [212-244] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-285] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-156] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-250] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-285] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-268] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-275] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [212-216] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-80] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-216] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-253] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-260] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-86] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-261] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-61] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-281] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-27] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-45] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-55] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-205] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-234] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-299] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-187] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-208] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-220] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-288] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-256] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-263] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-43] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-255] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-277] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-148] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-122] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-173] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-196] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-165] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-191] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-277] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-234] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-243] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-246] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-257] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-235] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-241] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-244] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-268] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-276] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-299] for track '31' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
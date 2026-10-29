# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_43`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_43/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 298 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 87: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - Row 88: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
> - Segment 'Action_ComboBlock' for track '7' has invalid range: start=149, end=147. Clamping end to start.
> - Segment 'Action_BlockSecondLevel' for track '7' has invalid range: start=172, end=147. Clamping end to start.
> - Action 'Action_PreSnap' range [0-278] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-216] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-298] for track '2' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [202-216] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-231] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-245] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-233] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-298] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-258] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-280] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-246] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-298] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-203] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-233] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-158] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-173] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-188] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-216] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '11' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-219] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-228] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-285] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-292] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-161] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-231] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-245] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-267] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-131] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-137] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-218] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-242] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-160] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-169] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-183] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-205] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-284] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-64] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-109] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-151] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-186] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-32] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-50] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-128] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-133] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-148] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-224] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-233] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-134] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [149-169] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [172-201] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [202-237] for track '23' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [242-261] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-192] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-195] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-236] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-199] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-222] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-199] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-275] for track '26' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-203] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-222] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-244] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-298] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-249] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-289] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-293] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-287] for track '33' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
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